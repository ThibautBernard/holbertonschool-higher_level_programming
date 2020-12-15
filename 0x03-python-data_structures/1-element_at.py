#!/usr/bin/python3
def element_at(my_list, idx):
    counter = 0
    if idx < 0:
        return None
    for i in my_list:
        if idx == counter:
            return i
        counter += 1
    return None
