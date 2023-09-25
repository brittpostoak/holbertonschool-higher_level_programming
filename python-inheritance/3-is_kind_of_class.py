#!/usr/bin/python3
"""
Function returns True if object is instance of a class that inherited from, otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Begins function - is_kind_of_class.
    """
    if isinstance(obj, a_class):
        return True
    return False
