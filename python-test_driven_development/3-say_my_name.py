#!/usr/bin/python3
"""
    Function that prints the name of a person.
"""


def say_my_name(first_name, last_name=""):
    """
        Args:
            first_name (string)
            last_name (string)

        Raises:
            TypeError: if first and last name aren't strings
        """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
