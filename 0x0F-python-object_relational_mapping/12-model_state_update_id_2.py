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


def change_state_obj(database):
    """change state name in database"""
    session = database[1]
    instance_a = session.query(State).filter(State.id == 2).one()
    instance_a.name = "New Mexico"
    session.add(instance_a)
    session.commit()

    session.close()
    database[0].dispose()

if __name__ == "__main__":
    change_state_obj(session_st())
