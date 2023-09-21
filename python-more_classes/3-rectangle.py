#!/usr/bin/python3

"""
Class that defines a rectangle.
"""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Get string representation."""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            for char in range(self.__width):
                string += '#'
            string += '\n'
        return string[:-1]
