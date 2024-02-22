#!/usr/bin/python3

"""
This module defines the Rectangle class that inherits from Base.
It includes methods for calculating the area, displaying the rectangle,
handling string representation, updating attributes, and converting
instance attributes to dictionary representation.
"""

from .base import Base


class Rectangle(Base):
    # Existing class code ...

    def display(self):
        """
        Represents a rectangle.
        Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x offset of the rectangle.
        y (int): The y offset of the rectangle.
        id (int): The id of the rectangle.
        """
        # Print the 'y' offset - vertical space before the rectangle
        print("\n" * self.y, end="")

        # Print each row of the rectangle
        for row in range(self.height):
            # 'x' offset: spaces before the '#' characters in each row
            print(" " * self.x + "#" * self.width)
