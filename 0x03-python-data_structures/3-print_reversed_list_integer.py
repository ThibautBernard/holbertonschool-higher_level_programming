#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newArray = my_list[::-1]
    for i in newArray:
        print("{:d}".format(i))
