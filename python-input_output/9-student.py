#!/usr/bin/python3
"""
Class Student that defines a student by age, first and last name.
"""


class Student():
    """Class to define student"""

    def __init__(self, first_name, last_name, age):
        """Begins function - initialize instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Begins function - to json"""
        return self.__dict__
