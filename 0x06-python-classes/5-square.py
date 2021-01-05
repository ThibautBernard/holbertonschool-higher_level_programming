#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """ Square class """
    def __init__(self, value=0):
        """ Initialize attributs
        Args: value (int): size of the square
        """
        self._size = value

    @property
    def size(self):
        """Getter size"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter size
        Args: value (int): size to check
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
        """Return the area size"""
        return self._size * self._size

    def my_print(self):
        """Print a square"""
        if (self._size == 0):
            print()
        else:
            for i in range(0, self._size):
                for x in range(0, self._size):
                    print("#", end="")
                print()
