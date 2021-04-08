#!/usr/bin/python3
"""
    find peak
"""


def find_peak(list_of_integers):
    """ sort the array and get the last """
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
