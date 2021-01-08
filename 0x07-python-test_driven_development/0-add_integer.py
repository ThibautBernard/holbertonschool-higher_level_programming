#!/usr/bin/python3
"""
add_integer - add two integer

"""


def add_integer(a, b=98):
    """ function that add two integer
    Args:
        a: (int, float): first int
        b: (int, float): second int
    """
    inf = float('inf')
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if a == inf:
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if b == inf:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
