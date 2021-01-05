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
        self.__size = value
        self.__position = position

    @property
    def size(self):
        """getter of size """
        return self.__size

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
            self.__size = value

    @property
    def position(self):
        """ getter of position """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter of position
        Args: value (tuples): int tuple to check
        """
        error = 0
        if (isinstance(value, tuple)):
            if (len(value) == 2):
                if (isinstance(value[0], int)):
                    if (isinstance(value[1], int)):
                        if (value[0] >= 0 and value[1] >= 0):
                            error = 1
        if error == 1:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return area"""
        return self.__size * self.__size

    def my_print(self):
        """print a square """
        if (self.__size == 0):
            print()
        else:
            for m in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for z in range(0, self.__position[0]):
                    print(" ", end="")
                for x in range(0, self.__size):
                    print("#", end="")
                print()
