#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def session_st():
    """inits session"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def parse(c):
    """parser for input"""
    CHARS = [';', "'", '"']
    for x in CHARS:
        c = c.replace(x, '--')
    return (c)


def print_state_names(database):
    """prints state id in database"""
    session = database[1]
    input_parsed = parse(sys.argv[4])
    instance_a = session.query(State).filter(State.name == input_parsed)
    try:
        print(instance_a[0].id)
    except:
        print("Not found")

    session.close()
    database[0].dispose()

if __name__ == "__main__":
    print_state_names(session_st())
