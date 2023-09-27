#!/usr/bin/python3
"""
Function that appends string at end of text file UTF8 and returns number 
of characters.
"""


def append_write(filename="", text=""):
    """Begins function - append write."""
    with open(filename, 'a') as f:
        return f.write(text)
