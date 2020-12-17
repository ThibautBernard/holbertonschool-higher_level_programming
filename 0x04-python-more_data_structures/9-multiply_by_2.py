#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = a_dictionary.copy()
    d.update((k, v * 2) for k, v in d.items())
    return d
