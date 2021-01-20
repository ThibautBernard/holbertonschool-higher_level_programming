#!/usr/bin/python3
"""function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ append_after """
    line = ""
    with open(filename, 'r', encoding='utf-8') as p:
        line = p.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for i in line:
            if search_string in i:
                i = i + new_string
            f.write(i)
