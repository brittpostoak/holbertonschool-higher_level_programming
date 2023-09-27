#!/usr/bin/python3
"""
Function that returns dictionary description with data 
structure for JSON serialization of object.
"""


def class_to_json(obj):
    """Begins function - class to json"""
    return obj.__dict__
