#!/usr/bin/python3
"""
Module with a script that lists all states from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys


def goto_db():
    """Inits a database"""
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3])
    return database


def filter_cities(database):
    """lists all cities of a given state in database"""
    name = sys.argv[4]
    clean = []
    cur = database.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY states.id ASC",
                (name,))
    get_rows = cur.fetchall()
    for row in get_rows:
        clean += row
    print(', '.join(clean))
    cur.close()
    database.close()

if __name__ == "__main__":
    filter_cities(goto_db())
