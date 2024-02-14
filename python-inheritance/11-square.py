#!/usr/bin/python3
""" a class BaseGeometry"""


class BaseGeometry:
    """ define a class BaseGeometry """
    def area(self):
        """ define area """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """mesure area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """define string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ __str__ define """
        return ("[Square] {}/{}".format(self.__size, self.__size))
