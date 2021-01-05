#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """
        Square class
    """
    def __init__(self, value=0):
        """ Initialize attributs
        Args: value (int): size of the square
        """
        self._size = value

    @property
    def size(self):
        """ getter of size
        """
        return self._size

    @size.setter
    def size(self, value):
        """ Setter of size
        Args: value (int): value to check
        """
        if (isinstance(value, int) is not True):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """Return the area of the square"""
        return self._size * self._size
