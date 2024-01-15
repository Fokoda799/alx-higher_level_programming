#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Geometry module"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
