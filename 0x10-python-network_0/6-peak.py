#!/usr/bin/python3
"""
    find peak
"""


def find_peak(list_of_integers):
    """
        Divide and conquer method
        split the array and subarray in two at each recursion
        return the peak if the peak is greather than his
        neighbors
    """
    if not list_of_integers:
        return None
    l = len(list_of_integers) - 1
    if l == 1:
        return list_of_integers[0]
    if l == 2:
        if list_of_integers[1] > list_of_integers[0]:
            return list_of_integers[1]
        else:
            return list_of_integers[0]
    mid = round(l / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
