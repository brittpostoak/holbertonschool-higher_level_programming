#!/usr/bin/python3
"""
Function that appends string at end of text file UTF8 and returns number 
of characters.
"""


def read_lines(filename="", nb_lines=0):
    """
    Begins function - read_lines.
    """
    n = []
    with open(filename, "r") as f:
        for index, line in enumerate(f):
            if index < nb_lines or nb_lines == 0:
                l.append(line)
            else:
                break
        print("{}".format("".join(n)), end="")
