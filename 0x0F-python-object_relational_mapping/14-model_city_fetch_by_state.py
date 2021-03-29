#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def session_st():
    """inits session"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def list_cities(database):
    """prints City obj in database"""
    session = database[1]
    instance_c = session.query(City, State).filter(State.id == City.state_id)
    for x, y in instance_c:
        print(y.name, ': ({}) '.format(x.id), x.name, sep='')

    session.close()
    database[0].dispose()

if __name__ == "__main__":
    list_cities(session_st())
