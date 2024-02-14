#!/usr/bin/python3
"""returns True if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """check inheritance """

    if isinstance(obj, a_class):

        return True
    return False
