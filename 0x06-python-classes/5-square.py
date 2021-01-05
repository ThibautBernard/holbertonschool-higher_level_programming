#!/usr/bin/python3
class Square:
    def __init__(self, value=0):
        self._size = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
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
        return self._size * self._size

    def my_print(self):
        if (self._size == 0):
            print()
        else:
            for i in range(0, self._size):
                for x in range(0, self._size):
                    print("#", end="")
                print()
