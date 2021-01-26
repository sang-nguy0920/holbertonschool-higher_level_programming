#!/usr/bin/python3
"""Base class module"""


import os
import json

class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Inits Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
