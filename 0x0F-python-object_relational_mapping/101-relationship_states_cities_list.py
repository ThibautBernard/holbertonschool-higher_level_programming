#!/usr/bin/python3
"""
    select all states and print
    all cities for each state
"""
import sys
import MySQLdb
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(State).all()
    for state in x:
        print("{:d}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {:d}: {}".format(city.id, city.name))
