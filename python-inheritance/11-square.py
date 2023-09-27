#!/usr/bin/python3
"""Class Square that inherits from Rectangle."""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Class for Square that inherits from Rectangle
    with method for area and string representation."""
    def __init__(self, size):
        """Initializes Square instance."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of Square."""
        return (self.__size * self.__size)

    def __str__(self):
        """String representation of Square."""
        str_rep = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return str_rep
