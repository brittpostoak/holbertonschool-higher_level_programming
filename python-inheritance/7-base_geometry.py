#!/usr/bin/python3
"""Defines class BaseGeomtry
with public instance methods for area and integer validation."""


class BaseGeometry:
    """Class with public instance method to raise exception
    and public instance method to validate integer."""
    def area(self):
        """Raises exception that area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
