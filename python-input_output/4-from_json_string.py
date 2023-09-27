#!/usr/bin/python3
"""
Function that returns object represented by a JSON string.
"""


def append_write(filename="", text=""):
    """
    Begins function - append_write.
    """
    with open(filename, encoding='utf-8', mode='a') as f:
        return f.write(text)
