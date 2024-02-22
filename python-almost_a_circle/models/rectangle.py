#!/usr/bin/python3

"""Module for the Rectangle class."""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Include your validation code here
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Include your validation code here
        self.__height = value

    # Add other properties and methods as needed

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.width * self.height
