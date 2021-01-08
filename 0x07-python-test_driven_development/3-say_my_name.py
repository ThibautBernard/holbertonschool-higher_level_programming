#!/usr/bin/python3
"""
say_my_name - print name and last name

"""


def say_my_name(first_name, last_name=""):
    """ function that print name and last name
    Args:
        first_name: (str): first name
        last_name: (str): last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name:
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
