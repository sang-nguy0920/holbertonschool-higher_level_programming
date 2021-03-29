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


def print_first_state(database):
    """prints 1st state object in database"""
    session = database[1]
    instance = session.query(State).first()
    try:
        print(instance.id, ': ', instance.name, sep='')
    except:
        print("Nothing")

    session.close()
    database[0].dispose()

if __name__ == "__main__":
    print_first_state(session_st())
