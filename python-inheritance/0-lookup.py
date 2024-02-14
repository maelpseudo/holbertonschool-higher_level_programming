#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list object containing the list of available attributes 
    and methods of an object.

    Args:
        obj (Any): The object to list attributes and methods for.

    Returns:
        list: A list of strings representing the names of the attributes 
              and methods of the object.
    """
    return dir(obj)
