#!/usr/bin/python3
"""
   Function that prints a square depending on the size of the parameter.
"""


def print_square(size):
    """
    Args:
        size: integer number

    Raises:
        TypeError: Size must be an integer
        ValueError: Size must be less than 0
        TypeError: Size is a float less than 0
    """

    if not isinstance(size, int):
        raise TypeError("Size must be an integer")

    if size < 0:
        raise ValueError("Size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("Size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
