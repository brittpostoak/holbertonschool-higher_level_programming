#!/usr/bin/python3
"""
Function that writes string to text file UTF8 and returns number of characters.
"""


def number_of_lines(filename=""):
    """
    Begins function - number_of_lines.
    """
    f = open(filename, 'r')
    for index, line in enumerate(f):
        pass
    return index + 1
