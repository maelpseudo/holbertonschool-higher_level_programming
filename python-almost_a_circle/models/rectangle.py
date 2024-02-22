#!/usr/bin/python3

"""
This module defines the Rectangle class that inherits from Base.
It includes methods for calculating the area, displaying the rectangle,
handling string representation, updating attributes, and converting
instance attributes to dictionary representation.
"""

from .base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x offset of the rectangle.
        y (int): The y offset of the rectangle.
        id (int): The id of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets/sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Gets/sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Assuming other methods like display() are also defined here

    def __str__(self):
        """
        Override the __str__ method to return a string representation
        of the Rectangle instance.
        Returns:
        str: string in the format "[Rectangle] (<id>)<x>/<y>-<width>/<height>".
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))
