#!/usr/bin/python3
"""Function that open/write and append a file"""


def append_write(filename="", text=""):
    """ Open/write append text in filename"""
    char_written = 0
    with open(filename, 'a', encoding='utf-8') as f:
        char_written = f.write(text)
    return char_written
