#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation"""
import json
to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(to_json_string(my_obj))
