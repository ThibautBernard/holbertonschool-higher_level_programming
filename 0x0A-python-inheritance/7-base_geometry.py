#!/usr/bin/python3
"""class base geometry"""


class BaseGeometry:
    """class baseGeometry class that does something"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ take a string and a value and we need to check what passed
        Args:
            name: (string): name of the string
            value: (integer): must be only a integer
        """
        if type(name) != str:
            name = "height"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
