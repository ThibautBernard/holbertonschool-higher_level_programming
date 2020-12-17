#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    d = max(a_dictionary.items())
    x = d[0]
    return x
