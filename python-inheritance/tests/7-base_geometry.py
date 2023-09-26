7-base_geometry.py Test File

   Function:
    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

    >>> geo = BaseGeometry()

    >>> geo.integer_validator("name", 1)

   Test: Greater than Zero
    >>> geo.integer_validator("name", -1)
    Traceback (most recent call last):
    ...
    ValueError: name must be greater than 0

   Test: Must be integer
    >>> geo.integer_validator("name", 1.1)
    Traceback (most recent call last):
    ...
    TypeError: name must be an integer

    >>> geo.integer_validator("name", "cat")
    Traceback (most recent call last):
    ...
    TypeError: name must be an integer

    >>> geo.area()
    Traceback (most recent call last):
    ...
    Exception: area() is not implemented
