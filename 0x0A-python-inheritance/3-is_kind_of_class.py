#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ check if object(obj) is instance of a specific (a_class) class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
