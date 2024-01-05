#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """ Rectangle Class """

    def __init__(self, height=0, width=0):
        """ Initialize a new Rectangle

            Args:
                height(int): The height of the rectangle
                width(int): The width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width Getter Method of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ width Setter Method of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height Getter Method of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ height Setter Method of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Return the Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Return the shape of # based on the h/w """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
