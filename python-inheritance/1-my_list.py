#!/usr/bin/python3
"""
Class MyList that inherits from list.
"""


class MyList(list):
    """
    Begin class - MyList.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        """
        print("{}".format(sorted(self)))
