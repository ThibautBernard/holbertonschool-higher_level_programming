#!/usr/bin/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square classes"""
    def __init__(self, size):
        """ Init function that initialize"""
        try:
            super().integer_validator("size", size)
            super().__init__(size, size)
            self.__size = size
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def __str__(self):
        """ Str method """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """ Return the area of the square"""
        return self.__size * self.__size
