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

    @property
    def width(self):
        """ Getter width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) is int:
            self.__width = value
        else:
            raise TypeError("Width must be an integer")

    @property
    def height(self):
        """ Getter height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError("Height must be an integer")

    @property
    def x(self):
        """ Getter x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter """
        if type(value) is int:
            self.__x = value
        else:
            raise TypeError("X must be an integer")

    @property
    def y(self):
        """ Getter x attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        if type(value) is int:
            self.__y = value
        else:
            raise TypeError("Y must be an integer")
