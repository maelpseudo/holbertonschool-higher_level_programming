#!/usr/bin/python3

class Rectangle:
    """A class Rectangle that defines a rectangle by:
    - Private instance attribute: width
    - Private instance attribute: height
    - Public class attribute number_of_instances
    - Public class attribute print_symbol
    - Instantiation with optional width and height
    - Method to calculate area of the rectangle
    - Method to calculate perimeter of the rectangle
    - __str__ method to print the rectangle with the character(s) stored in print_symbol
    - __repr__ method to return a string representation of the rectangle
    - __del__ method to print a message when an instance is deleted
    - Static method to return the biggest rectangle based on the area
    - Class method to return a new Rectangle instance with width == height == size
    """
    
    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute initialized to #

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle.
        If width or height is 0, the perimeter is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)  # Convert print_symbol to string to handle all types
        rectangle_str = "\n".join([symbol * self.__width for _ in range(self.__height)])
        return rectangle_str

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
