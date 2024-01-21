#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
from turtle import *


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        list_dict = []
        if not list_objs:
            return json.dump(filename, [], indent=2)
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        json_rpe = Base.to_json_string(list_dict)
        with open(filename, 'w') as file:
            file.write(json_rpe)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        with open(filename, 'w') as c:
            writer = csv.DictWriter(c, fieldnames=list_dict[0].keys())
            writer.writeheader()
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        list_dict = []
        try:
            with open(filename, 'r') as file:
                dict_reader = csv.DictReader(file)
                for row in dict_reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    list_dict.append(row)
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        setup(800, 500)
        bgcolor("blue")
        for rect in list_rectangles:
            od = rect.to_dictionary()
            penup()
            goto(od['x'], od['y'])
            pendown()
            color("red")
            begin_fill()
            for i in range(2):
                fd(od['width'])
                lt(90)
                fd(od['height'])
                lt(90)
            end_fill()

        for squ in list_squares:
            od = squ.to_dictionary()
            penup()
            goto(od['x'], od['y'])
            pendown()
            color("green")
            begin_fill()
            for i in range(4):
                fd(od['size'])
                lt(90)
            end_fill()
        done()
