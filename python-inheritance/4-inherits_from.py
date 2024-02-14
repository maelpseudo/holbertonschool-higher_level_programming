#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or
    indirectly) from the specified class, excluding direct instances of the
    specified class.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of a class that inherited from
              the specified class (excluding direct instances), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
