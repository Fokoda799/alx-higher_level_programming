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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    def display(self):
        """Display the rectangle"""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """Update attrs"""
        if len(args) != 0:
            for i, dic in enumerate(self.__dict__):
                self.__dict__[dic] = args[i]
                if (len(args) - i) == 1:
                    break

        elif len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                else:
                    raise TypeError(f"No attr named {key}")
