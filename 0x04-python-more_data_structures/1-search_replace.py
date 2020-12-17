#!/usr/bin/python3
def search_replace(my_list, search, replace):
    counter = 0
    new = []
    for i in my_list:
        if i == search:
            new.append(replace)
        else:
            new.append(i)
        counter += 1
    return new
