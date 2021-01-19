#!/usr/bin/python3
""" funciton is_same_class"""


def is_same_class(obj, a_class):
    """ check if object(obj) is instance of a specific (a_class) class
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
