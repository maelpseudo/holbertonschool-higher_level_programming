#!/usr/bin/python3
""" Definition of a custom list class """


class MyList(list):
    """  A custom list class that inherits from the built-in list class """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
