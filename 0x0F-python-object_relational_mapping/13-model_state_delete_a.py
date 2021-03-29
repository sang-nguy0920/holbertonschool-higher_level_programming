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


def delete_state_obj(database):
    """deletes state obj name a in database"""
    session = database[1]
    instance_a = session.query(State).filter(State.name.like('%a%'))
    for x in instance_a:
        session.delete(x)
    session.commit()

    session.close()
    database[0].dispose()

if __name__ == "__main__":
    delete_state_obj(session_st())
