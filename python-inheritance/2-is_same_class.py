#!/usr/bin/python3
"""
   returns True if the object is exactly an instance
"""

def is_same_class(obj, a_class):
    """ check if an object is exactly an instance of a class """
    return type(obj) is a_class
