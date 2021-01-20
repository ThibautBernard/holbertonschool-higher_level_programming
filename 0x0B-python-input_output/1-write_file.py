#!/usr/bin/python3
"""Function that open/write a file"""


def write_file(filename="", text=""):
    """ Open/write text in filename"""
    char_written = 0
    with open(filename, 'w', encoding='utf-8') as f:
        char_written = f.write(text)
    return char_written
