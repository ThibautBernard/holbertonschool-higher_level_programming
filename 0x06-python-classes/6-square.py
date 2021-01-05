#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """Square class"""
    def __init__(self, value=0, position=(0, 0)):
        """Initialize attributs
        Args:
            value: (int): size of the sqaure
            position: (tuples): int tuple
        """
        self._size = value
        self._position = position

    @property
    def size(self):
        """getter of size """
        return self._size

    @size.setter
    def size(self, value):
        """setter of size
        Args: value (int): value to check
        """
        if (isinstance(value, int) is not True):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        """ getter of position """
        return self._position

    @position.setter
    def position(self, value):
        """ setter of position
        Args: value (tuples): int tuple to check
        """
        count = 0
        no_error = 0
        if (isinstance(value, tuple)):
            if (len(value) == 2):
                if (isinstance(value[0], int)):
                    if (isinstance(value[1], int)):
                        if (value[0] >= 0 and value[1] >= 0):
                            no_error += 1
        if no_error == 1:
            self._position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return area"""
        return self._size * self._size

    def my_print(self):
        """print a square """
        if (self._size == 0):
            print()
        else:
            for m in range(self._position[1]):
                print()
            for i in range(0, self._size):
                for z in range(0, self._position[0]):
                    print(" ", end="")
                for x in range(0, self._size):
                    print("#", end="")
                print()
