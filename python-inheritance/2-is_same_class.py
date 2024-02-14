#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to match the object's type against.

    Returns:
        bool: True if the object is exactly an instance of the specified class, 
              otherwise False.
    """
    return type(obj) is a_class
