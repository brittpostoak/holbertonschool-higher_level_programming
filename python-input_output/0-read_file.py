#!/usr/bin/python3
"""
Function that reads a text file UTF8 and prints it to stdout.
"""


def read_file(filename=""):
    """Begins function - read file"""
    with open(filename) as f:
        print(f.read(), end="")
