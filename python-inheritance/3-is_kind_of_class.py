#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a 
    class that inherited from, the specified class.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class or a class
              that inherited from the specified class, otherwise False.
    """
    return isinstance(obj, a_class)
