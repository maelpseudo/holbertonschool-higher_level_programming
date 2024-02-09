#!/usr/bin/python3
"""function that adds two integers"""


def add_integer(a, b=98):
    """define add function"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b