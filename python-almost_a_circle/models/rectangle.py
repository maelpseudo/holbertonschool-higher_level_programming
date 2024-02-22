#!/usr/bin/python3

from .base import Base


class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x offset of the rectangle.
        y (int): The y offset of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x offset of the rectangle.
            y (int): The y offset of the rectangle.
            id (int): An optional integer to be used as
            the unique id (inherited from Base).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        # Include validation that value is an integer greater than 0
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        # Include validation that value is an integer greater than 0
        self.__height = value

    @property
    def x(self):
        """int: Gets or sets the x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        # Include validation that value is an integer >= 0
        self.__x = value

    @property
    def y(self):
        """int: Gets or sets the y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        # Include validation that value is an integer >= 0
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Affiche le rectangle en utilisant le caractère `#`.
        """
        # Ajout de lignes vides pour 'y'
        print("\n" * self.y, end="")

    # Construction et affichage de chaque ligne du rectangle
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Retourne la représentation en chaîne de caractères de Rectangle.

        Retourne:
            str: Une représentation en chaîne de l'instance.
        """
        base_str = "[Rectangle] ({}){}/{}-"
        formatted = base_str.format(self.id, self.x, self.y)
        dimensions = "{}/{}".format(self.width, self.height)
        return formatted + dimensions

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args : New attribute values in the
            order of id, width, height, x, y.
            **kwargs (Optional): New attribute values by key.
        """
        attributes = ["id", "width", "height", "x", "y"]
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

        if not args:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the Rectangle instance into a dictionary representation.

        Returns:
            dict: A dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
