#!/usr/bin/python3
"""
Class MyList that inherits from list.
"""


class MyList(list):
    """
    Begins class - MyList.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        """
        copy_list = self.copy()
        copy_list.sort()
        print(copy_list)
