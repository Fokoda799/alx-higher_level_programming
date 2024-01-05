#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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
        re = []
        for i in range(self.__height):
            [re.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                re.append("\n")
        return ("".join(re))

    def __repr__(self):
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            return TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            return TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
