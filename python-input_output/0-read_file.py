#!/usr/bin/python3
"""
Function that reads a text file UTF8 and prints it to stdout.
"""


def read_file(filename=""):
    """
    Begins function - read_file.
    """
    f = open(filename, 'r')
    for line in f:
        print('{}'.format(line), end='')
