#!/usr/bin/python3
"""
Class Base - The base of all the classes
Id counter
"""
import json
import os.path
from os import path
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """write json representation to a file"""
        if list_objs is None or len(list_objs) == 0:
            with open("{}.json".format(cls.__name__), "a") as file:
                    file.write("[]")
        else:
            a = []
            for i in list_objs:
                a.append(i.to_dictionary())

            with open("{}.json".format(type(i).__name__), "w") as file:
                s = Base.to_json_string(a)
                file.write(s)

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            if type(list_dictionaries) is list:
                return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation """
        if type(json_string) is str:
            if len(json_string) == 0:
                return []
            return json.loads(json_string)
        if json_string is None:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes from dictionary"""
        if type(dictionary) is dict and dictionary is not None:
            r = cls(1, 1)
            r.update(**dictionary)
            return r

    @classmethod
    def load_from_file(cls):
        """  returns an instance with all attributes"""
        list_instance = []
        if path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), "r") as f:
                for i in f:
                    count = 0
                    list_object_length = len(cls.from_json_string(i))
                    for x in range(0, list_object_length):
                        data = cls.from_json_string(i)[count]
                        instance = cls.create(**data)
                        list_instance.append(instance)
                        count += 1
            return list_instance
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of object into csv """
        with open("{}.csv".format(cls.__name__), 'a') as file:
            if cls.__name__ == "Rectangle":
                a = []
                for i in list_objs:
                    a.extend([i.id, i.width, i.height, i.x, i.y])
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
                    a.clear()
            if cls.__name__ == "Square":
                a = []
                for i in list_objs:
                    a.extend([i.id, i.size, i.x, i.y])
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow(a)
                    a.clear()

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv to object"""
        exist_class = ["Rectangle", "Square"]
        if cls.__name__ in exist_class:
            with open("{}.csv".format(cls.__name__), 'r') as file:
                content_f = csv.reader(file)
                arr_object = []
                for i in content_f:
                    instance = cls(1, 1)
                    tmp = []
                    for y in i:
                        tmp.append(int(y))
                    instance.update(*tmp)
                    arr_object.append(instance)
            return arr_object
