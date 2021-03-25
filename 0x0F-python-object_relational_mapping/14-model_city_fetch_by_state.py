#!/usr/bin/python3
"""
    query all data from table city and fetch state linked with
    city
"""
import sys
import MySQLdb
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = session.query(City).all()
    for i in city:
        name_state = session.query(State).\
         filter(State.id == i.state_id).first().name
        print("{}: ({:d}) {}".format(name_state, i.id, i.name))
