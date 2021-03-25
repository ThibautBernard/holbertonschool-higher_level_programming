#!/usr/bin/python3
"""
    delete all object State where name has a 'a' in,
    and commit the changes into the database
"""
import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    list_to_del = session.query(State).filter(State.name.ilike("%a%")).all()
    for i in list_to_del:
        session.delete(i)
    session.commit()
