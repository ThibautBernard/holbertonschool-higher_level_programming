#!/usr/bin/python3
"""
    select all states and display each cities from this
    state
"""
import sys
import MySQLdb
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="California")
    c = City(name="San Francisco", state=new)
    session.add(c)
    session.add(new)
    session.commit()
