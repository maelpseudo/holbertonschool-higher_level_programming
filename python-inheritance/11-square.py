#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area method and integer_validator.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)

class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """
    def __init__(self, size):
        super().__init__(size, size)  # Initialize Rectangle with size as both width and height
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        # Ensure the class name is Square instead of Rectangle
        return "[Square] {}/{}".format(self.__size, self.__size)
