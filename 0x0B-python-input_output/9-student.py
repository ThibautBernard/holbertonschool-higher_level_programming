#!/usr/bin/python3
"""Clss student"""


class Student:
    """Class of a student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionnary of all the attributes"""
        return self.__dict__
