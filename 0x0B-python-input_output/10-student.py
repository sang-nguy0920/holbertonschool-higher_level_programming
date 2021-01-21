#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """inits"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary repres of a Student instance"""
        d = {}
        if attrs is None:
            return self.__dict__
        for x in attrs:
            if hasattr(self, x):
                d[x] = getattr(self, x)
        return d
