#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    arr = []
    for key, val in a_dictionary.items():
        if val == value:
            arr.append(key)
    for i in arr:
        a_dictionary.pop(i)
    return a_dictionary
