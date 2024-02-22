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
        Prints the Rectangle instance with the '#' character, taking care of 'x' and 'y' offsets.
        """
        # Print the 'y' offset - vertical space before the rectangle
        print("\n" * self.y, end="")

        # Print each row of the rectangle
        for row in range(self.height):
            # 'x' offset: spaces before the '#' characters in each row
            print(" " * self.x + "#" * self.width)
