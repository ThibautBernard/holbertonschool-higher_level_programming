#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """Square class"""
    def __init__(self, value=0):
        """Initialize attributs
        Args:
            value: (int): size of the sqaure
            position: (tuples): int tuple
        """
        self.size = value

    def __eq__(self, other):
        """ compare object
        Args:
            other (object): object to compare
        """
        return ((self.size) == (other.size))

    def __ne__(self, other):
        """ compare object
        Args:
            other (object): object to compare
        """
        return ((self.size) != (other.size))

    def __lt__(self, other):
        """ compare object
        Args:
            other (object): object to compare
        """
        return ((self.size) < (other.size))

    def __le__(self, other):
        """ compare object
        Args:
            other (object): object to compare
        """
        return ((self.size) <= (other.size))

    def __gt__(self, other):
        """ compare object
        Args:
            other (object): object to compare
        """
        return ((self.size) > (other.size))

    def __ge__(self, other):
        """ compare object
        Args:
            other (object): object to compare
        """
        return ((self.size) >= (other.size))

    @property
    def size(self):
        """getter of size """
        return self._size

    @size.setter
    def size(self, value):
        """setter of size
        Args: value (int): value to check
        """
        if (not isinstance(value, int) and not isinstance(value, float)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """return square area """
        return self.__size * self.__size
