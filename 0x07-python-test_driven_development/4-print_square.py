#!/usr/bin/python3
"""
print_square - print a square

"""


def print_square(size):
    """ function that print a square from size
    Args:
        size: (int): size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for y in range(0, size):
            print("#", end="")
        print()
