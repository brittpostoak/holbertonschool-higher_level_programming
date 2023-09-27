#!/usr/bin/python3
"""
Class Student that defines a student by age, first and last name.
"""


class Student:
    """Begin function - initialize"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To JSON"""
        return self.__dict__
