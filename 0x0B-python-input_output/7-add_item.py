#!/usr/bin/python3
import sys
import os.path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if not os.path.isfile('add_item.json'):
    l = []
    save_to_json_file(l, "add_item.json")

l = load_from_json_file("add_item.json")

counter = 0
for i in sys.argv:
    if counter != 0:
        l.append(i)
    counter += 1
save_to_json_file(l, "add_item.json")
