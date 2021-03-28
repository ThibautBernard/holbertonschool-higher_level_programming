#!/usr/bin/python3
"""
    ORM Mapper to tables States
"""
import sys
import MySQLdb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# from relationship_city import City
Base = declarative_base()


class State(Base):
    """Map state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    c = "City"
    cities = relationship(c, backref="state", cascade="all, delete")
