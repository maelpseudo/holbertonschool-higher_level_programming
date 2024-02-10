#!/usr/bin/python3
"""Define a class representing a rectangle"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    - width (int): represent the width of the rectangle.
    - height (int): represent the height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with the given width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns string representation"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += '#' * self.width + '\n'
        return string[:-1]

    def __repr__(self):
        heightR = self.__height
        widthR = self.__width
        return "Rectangle({}, {})".format(widthR, heightR)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
