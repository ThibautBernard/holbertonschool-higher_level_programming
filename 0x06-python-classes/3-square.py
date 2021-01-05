#!/usr/bin/python3
"""
Square class - setter and initialize the class

"""


class Square:
    """
        Square class
    """
    def __init__(self, size=0):
        """ Initialize
        Args:
            size (int): size of the square

        """
        self.set_size(size)

    def set_size(self, s):
        """
            setter of the size
        Args:
            s (int): size passed to check
        """
        try:
            if (s < 0):
                raise ValueError
            if (isinstance(s, int) is not True):
                raise TypeError
            else:
                self.__size = s
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """
            Return the area
        """
        return self.__size * self.__size
