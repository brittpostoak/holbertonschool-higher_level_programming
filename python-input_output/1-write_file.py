#!/usr/bin/python3
"""
Function that writes string to text file UTF8 and returns 
number of characters.
"""


def write_file(filename="", text=""):
    """
    Begins function - write file.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)

    return len(text)
