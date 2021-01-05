#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """ square class """
    def __init__(self, value=0, position=(0, 0)):
        """Initialize attributs
        Args:
            value (int): size of square
            position (tuples): position
        """
        self._size = value
        self._position = position

    def __str__(self):
        """ invoke print method if print() use on the instance"""
        self.my_print()
        return ""

    @property
    def size(self):
        """getter """
        return self._size

    @size.setter
    def size(self, value):
        """setter"""
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

    @property
    def position(self):
        """getter"""
        return self._position

    @position.setter
    def position(self, value):
        """setter"""
        try:
            for i in value:
                if (isinstance(i, int) is not True):
                    raise TypeError
            self._position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """Return Area """
        return self._size * self._size

    def my_print(self):
        """Print square"""
        counter = 0
        if (self._size == 0):
            print()
        else:
            for i in range(0, self._size):
                for z in range(0, self._position[0]):
                    print(" ", end="")
                for x in range(0, self._size):
                    print("#", end="")
                counter += 1
                if counter != self._size:
                    print()
