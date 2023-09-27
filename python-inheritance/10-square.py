#!/usr/bin/python3
"""Class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle
    with method for area."""
    def __init__(self, size):
        """Initializes Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of Square."""
        return (self.__size * self.__size)
