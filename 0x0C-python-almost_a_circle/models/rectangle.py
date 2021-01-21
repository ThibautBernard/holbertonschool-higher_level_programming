#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle that inherit from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.__width * self.__height

    @property
    def width(self):
        """ Getter width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Getter height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ Getter x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ Getter x attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
