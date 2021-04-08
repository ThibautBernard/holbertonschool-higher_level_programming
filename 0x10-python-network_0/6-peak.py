#!/usr/bin/python3
"""
    find peak
"""


def find_peak(list_of_integers):
    """
        sort the array and return the last element
        O(n log(n))
    """
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
