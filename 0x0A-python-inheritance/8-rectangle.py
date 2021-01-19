#!/usr/bin/python3
""" class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle that inerith from BaseGeometry"""
    def __init__(self, width, height):
        """Init function that initialize"""
        self.__width = self.integer_validator(width, height)
        self.__height = self.integer_validator(width, height)
