#!/usr/bin/python3
""" base """
import json
import turtle


class Base:
    """ base """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation"""
        Base.__nb_objects += 1

        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convertit la liste des dictionnaires en chaîne JSON."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Sauvegarde la liste des objets dans un fichier JSON."""
        list_dicts = []
        if list_objs:
            for v in list_objs:
                list_dicts.append(v.to_dictionary())

        with open('%s.json' % (cls.__name__), 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Charge la chaîne JSON en liste."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Crée une instance à partir d'un dictionnaire."""
        if 'rectangle' in cls.__name__.lower():
            obj = cls(1, 1)
        else:
            obj = cls(1)

        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """Charge les instances à partir d'un fichier JSON."""
        try:
            with open('%s.json' % (cls.__name__), 'r') as file:
                data = file.read()
        except FileNotFoundError:
            return []

        data = cls.from_json_string(data)
        return [cls.create(**v) for v in data]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Dessine les rectangles et carrés avec Turtle."""
        w = turtle.Screen()
        w.bgcolor('yellow')
        w.title('Almost a circle')

        t = turtle.Turtle()
        t.up()
        t.clear()

        for obj in list_rectangles + list_squares:
            p = (obj.x, obj.y)
            t.goto(p)
            t.down()
            for _ in range(2):
                t.forward(obj.width)
                t.left(90)
                t.forward(obj.height)
                t.left(90)
            t.up()
