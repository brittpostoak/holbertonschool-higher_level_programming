#!/usr/bin/python3
"""
Class Student that defines a student by age, first and last name.
"""


def class_to_json(obj):
    """
    Begins function - class to json
    """

    if hasattr(obj, '__dict__'):
        return obj.__dict__
