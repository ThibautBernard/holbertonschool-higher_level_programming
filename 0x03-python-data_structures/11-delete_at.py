#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    new_list = []
    counter = 0
    numb = 0
    for i in my_list:
        if idx == counter:
            numb = i
        counter += 1
    my_list.remove(numb)
    return my_list
