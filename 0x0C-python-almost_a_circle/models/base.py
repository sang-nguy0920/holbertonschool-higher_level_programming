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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_object = []
        if list_objs is not None:
            for i in list_objs:
                list_object.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_object))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string rep. json_string"""
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        list_instances = []
        if os.path.isfile(filename):
            with open(filename) as f:
                io = cls.from_json_string(f.read())
                for id in io:
                    list_instances.append(cls.create(**id))
                return list_instances
        else:
            return []
