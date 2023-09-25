#!/usr/bin/python3
"""
Function returns True if object is exact instance of specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Begins function - is_same_class.
    """
    if type(obj) is a_class:
        return True
    return False
