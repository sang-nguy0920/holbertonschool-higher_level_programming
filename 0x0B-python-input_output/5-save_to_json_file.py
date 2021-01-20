#!/usr/bin/python3
"""
function that writes an Object to a text file,
using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json_file = json.dumps(my_obj)
        f.write(json_file)
