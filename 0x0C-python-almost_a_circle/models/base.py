#!/usr/bin/python3
"""
Class Base - The base of all the classes
Id counter
"""
import json


class Base:
    """
        Class that have a private attribute class
        that count the number of objects instanced
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return json representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            if type(list_dictionaries) == dict:
                return json.dumps(list_dictionaries)
