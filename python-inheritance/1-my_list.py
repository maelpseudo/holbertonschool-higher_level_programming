#!/usr/bin/python3

class MyList(list):
    """
    MyList class that inherits from list.

    Methods:
        print_sorted(self): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
