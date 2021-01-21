#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename) as f:
        json_ob = json.load(f)
    return json_ob
