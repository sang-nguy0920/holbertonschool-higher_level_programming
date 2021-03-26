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


def list_states(database):
    """lists all states in database"""
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{:s}' \
                ORDER BY id ASC".format(sys.argv[4]))
    get_rows = cur.fetchall()
    for row in get_rows:
            print(row)
    cur.close()
    database.close()

if __name__ == "__main__":
    list_states(goto_db())
