#!/usr/bin/python3
"""
Function that returns JSON representation of an object.
"""


def write_file(filename="", text=""):
    """
    Begins function - write_file.
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        return f.write(text)
