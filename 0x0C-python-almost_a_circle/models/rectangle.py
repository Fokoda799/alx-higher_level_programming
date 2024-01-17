#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes"""
        dict = {'width': width, 'height': height, 'x': x, 'y': y}
        for attr in dict:
            self.int_validation(attr, dict[attr])
            self.pos_validation(attr, dict[attr])
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @property
    def height(self):
        """height Getter"""
        return self.__height

    @property
    def x(self):
        """x Getter"""
        return self.__x

    @property
    def y(self):
        """y Getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width Setter"""
        self.int_validation('width', value)
        self.pos_validation('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        """height Setter"""
        self.int_validation('height', value)
        self.pos_validation('height', value)
        self.__height = value

    @x.setter
    def x(self, value):
        """x Setter"""
        self.int_validation('x', value)
        self.pos_validation('x', value)
        self.__x = value

    @y.setter
    def y(self, value):
        """y Setter"""
        self.int_validation('y', value)
        self.pos_validation('y', value)
        self.__y = value

    def int_validation(self, attr_name, value):
        """Integer validation"""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")

    def pos_validation(self, attr_name, value):
        """Positive validation"""
        if attr_name in ['width', 'height']:
            if value <= 0:
                raise ValueError(f"{attr_name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        """The area of rectangle"""
        return self.width * self.height
