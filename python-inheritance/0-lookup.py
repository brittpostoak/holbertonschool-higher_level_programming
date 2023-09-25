#!/usr/bin/python3
"""
Returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Get a list of all the available attributes and methods of the object.
    """
    return list(dir(obj))
