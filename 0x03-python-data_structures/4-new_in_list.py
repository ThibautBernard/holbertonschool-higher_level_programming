#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]
    if idx < 0:
        return cpy_list
    counter = 0
    for i in cpy_list:
        if counter == idx:
            cpy_list[counter] = element
            return cpy_list
        counter += 1
    return cpy_list
