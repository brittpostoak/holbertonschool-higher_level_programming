#!/usr/bin/python3
"""
Class Student that defines a student by age, first and last name.
"""


class Student():
    """Class to define Student."""

    def __init__(self, first_name, last_name, age):
        """Begins function - initialize instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Begins function - to json."""
        if type(attrs) is list:
            new_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__
