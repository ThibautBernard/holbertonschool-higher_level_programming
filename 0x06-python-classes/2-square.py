#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize
        Args:
            size (int): the size of the square
        """
        if (isinstance(size, int) is not True):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
