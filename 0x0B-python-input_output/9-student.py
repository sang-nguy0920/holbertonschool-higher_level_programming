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

    def to_json(self):
        """retrieves a dictionary repres of a Student instance"""
        return self.__dict__
