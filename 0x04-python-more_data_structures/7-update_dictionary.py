#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    count = 0
    for k, v in a_dictionary.items():
        if k == key:
            a_dictionary[k] = value
            count += 1
        if count == 0:
            a_dictionary[key] = value
    return a_dictionary
