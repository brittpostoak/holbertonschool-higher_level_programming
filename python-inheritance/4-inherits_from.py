#!/usr/bin/python3
"""
Function that returns True if object is instance of class inherited from specified class.
"""


def inherits_from(obj, a_class):
    """
    Begins fuction - inherits_from.
    """
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
