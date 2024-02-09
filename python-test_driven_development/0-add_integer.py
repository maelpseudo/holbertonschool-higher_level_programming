#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    
    Parameters:
    a (int, float): The first number to add. Must be an integer or float.
    b (int, float, optional): The second number to add. Must be an integer or float. Defaults to 98.
    
    Returns:
    int: The sum of a and b, with both numbers casted to integers if they were floats.
    
    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
