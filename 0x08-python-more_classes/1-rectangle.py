#!/usr/bin/python3
"""
Rectangle class - define a rectangle
"""


class Rectangle:
    """ class rectangle that create a rectangle"""
    def __init__(self, width=0, height=0):
        """ constructor function
        Args:
            width: (int): width of Rectangle
            height: (int): heigth of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width
        Args:
            value: (int): width to check and change with
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ setter height
        Args:
            value: (int): height to check and change with
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
