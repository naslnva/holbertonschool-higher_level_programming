#!/usr/bin/python3
"""This module defines a class MyList that inherits from list"""


class MyList(list):
    """MyList is a subclass of list that adds a print_sorted method"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
