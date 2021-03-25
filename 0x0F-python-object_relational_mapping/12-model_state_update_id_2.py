#!/usr/bin/python3
"""
    update object State and commit the changes into the database
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
    state_to_change = session.query(State).filter_by(id=2).first()
    state_to_change.name = "New Mexico"
    session.commit()
