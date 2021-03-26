#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def session_st():
    """fill in later for checker"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def list_states(database):
    """lists all states in database"""
    session = database[1]
    for instance in session.query(State).order_by(State.id):
        print(instance.id, ': ', instance.name, sep='')

    session.close()
    database[0].dispose()

if __name__ == "__main__":
    list_states(session_st())
