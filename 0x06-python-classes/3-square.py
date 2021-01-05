#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.set_size(size)

    def set_size(self, s):
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
        return self.__size * self.__size
