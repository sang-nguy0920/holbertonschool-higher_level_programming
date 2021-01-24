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
