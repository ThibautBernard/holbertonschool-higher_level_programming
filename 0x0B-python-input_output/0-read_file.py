#!/usr/bin/python3
"""Function that open/read a file and display"""


def read_file(filename=""):
    """ Open/Read and display the content of the file"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
