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
        try:
            if (value < 0):
                raise ValueError
            if (isinstance(value, int) is not True):
                raise TypeError
            else:
                self._size = value
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")

    def area(self):
        """Return the area of the square"""
        return self._size * self._size
