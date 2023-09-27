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

    def to_json(self, attrs=None):
        """Begins function - to json"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """Begins function - reload from json"""
        for key, value in json.items():
            setattr(self, key, value)
