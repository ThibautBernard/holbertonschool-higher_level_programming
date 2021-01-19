#!/usr/bin/python3
""" class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle that inerith from BaseGeometry"""
    def __init__(self, width, height):
        """Init function that initialize"""
        try:
            super().integer_validator("width", width)
            super().integer_validator("height", height)
            self.__width = width
            self.__height = height
        except Exception as e:
                print("[{}] {}".format(e.__class__.__name__, e))

    def __str__(self):
        """str fucnction """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ return the area of the rectangle"""
        return self.__width * self.__height
