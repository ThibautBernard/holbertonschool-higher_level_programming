#!/usr/bin/python3
class Square:
    def __init__(self, value=0, position=(0, 0)):
        self._size = value
        self._position = position

    def __str__(self):
        self.my_print()
        return ""

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        try:
            for i in value:
                if (isinstance(i, int) is not True):
                    raise TypeError
            self._position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        return self._size * self._size

    def my_print(self):
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
