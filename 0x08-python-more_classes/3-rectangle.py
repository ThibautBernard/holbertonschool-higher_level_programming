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
        self.__width = width
        self.__height = height

    def __str__(self):
        """ string representation of the object """
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(0, self.__height):
            for y in range(0, self.__width):
                s += "#"
            if i + 1 != self.__height:
                s += "\n"
        return s

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

    def area(self):
        """ return area rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return perimeter rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
