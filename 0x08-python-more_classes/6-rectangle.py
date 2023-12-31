#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return the area"""
        return self.__height * self.__width

    def perimeter(self):
        """ Return the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Return the shape of # based on the h/w """

        if self.__height == 0 or self.__width == 0:
            return ("")
        rectangle_shape = []
        for i in range(self.__height):
            [rectangle_shape.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle_shape.append("\n")
        return ("".join(rectangle_shape))

    def __repr__(self):
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
