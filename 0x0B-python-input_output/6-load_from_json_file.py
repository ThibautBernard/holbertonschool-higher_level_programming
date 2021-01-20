#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”:"""
import json
to_json_string = __import__('3-to_json_string').to_json_string


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:"""
    value = ""
    with open(filename, 'r', encoding='utf-8') as f:
        value = f.read()
    return json.loads(value)
