#!/usr/bin/python3

"""
This module defines the Rectangle class that inherits from Base.
It includes methods for calculating the area, displaying the rectangle,
handling string representation, updating attributes, and converting
instance attributes to dictionary representation.
"""

from models.base import Base


class Rectangle(Base):
    """
    Classe Rectangle qui hérite de Base, représentant un rectangle.
    Attributs:
        width (int): Largeur du rectangle.
        height (int): Hauteur du rectangle.
        x (int): Décalage horizontal du rectangle (à gauche).
        y (int): Décalage vertical du rectangle (en haut).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise une nouvelle instance de Rectangle.
        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
            x (int): Le décalage horizontal du rectangle.
            y (int): Le décalage vertical du rectangle.
            id (int): L'identifiant unique du rectangle, hérité de Base.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Obtient ou définit la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Obtient ou définit la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Obtient ou définit le décalage horizontal du rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Obtient ou définit le décalage vertical du rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calcule l'aire du rectangle.
        Returns:
            L'aire du rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Affiche l'instance de Rectangle en utilisant le caractère '#',
        en prenant en compte les décalages 'x' et 'y'.
        """
        print("\n" * self.y, end='')
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères
        de l'instance de Rectangle,
        en format "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
        """
        part1 = f"[Rectangle] ({self.id})"
        part2 = f" {self.x}/{self.y} - {self.width}/{self.height}"
        return part1 + part2

    def update(self, *args, **kwargs):
        """
        Met à jour les attributs de l'instance de Rectangle.
        Args:
            *args: Nouvelles valeurs des attributs dans un ordre spécifique:
                - 1er argument représente id
                - 2ème argument représente width
                - 3ème argument représente height
                - 4ème argument représente x
                - 5ème argument représente y
            **kwargs: Nouvelles valeurs des attributs par clé.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for attr, value in zip(attrs, args):
            setattr(self, attr, value)
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Retourne le dictionnaire représentant l'instance de Rectangle.
        Returns:
            Un dictionnaire contenant tous les attributs de l'instance.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
