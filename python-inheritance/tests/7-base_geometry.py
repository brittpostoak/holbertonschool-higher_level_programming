7-base_geometry.py Test File

   Function:
    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()

   Test: Instantiation.
    >>> print(bg.__dict__)
    {}

   Test: Area method.
    >>> try:
    bg.area()
    except Exception as err:
    print(err)
    area() is not implemented

   Test: Integer_validator method.
    >>> try:
    bg.integer_validator("x", 1)
    except Exception as err:
    print(err)

   Test: Integer_validator method with TypeError float.
    >>> try:
    bg.integer_validator("x", 3.14159)
    except Exception as err:
    print(err)
    x must be an integer

   Test: Integer_validator method with TypeError string.
    >>> try:
    bg.integer_validator("x", "52")
    except Exception as err:
    print(err)
    x must be an integer

   Test: Integer_validator method with TypeError tuple.
    >>> try:
    bg.integer_validator("x", (0,))
    except Exception as err:
    print(err)
    x must be an integer

   Test: Integer_validator method with TypeError list.
    >>> try:
    bg.integer_validator("x", [7])
    except Exception as err:
    print(err)
    x must be an integer

   Test: Integer_validator method with TypeError boolean.
    >>> try:
    bg.integer_validator("x", True)
    except Exception as err:
    print(err)
    x must be an integer

   Test: Integer_validator method with TypeError set.
    >>> try:
    bg.integer_validator("x", {8})
    except Exception as err:
    print(err)
    x must be an integer

   Test: Integer_validator method with ValueError negative.
    >>> try:
    bg.integer_validator("x", -2)
    except Exception as err:
    print(err)
    x must be greater than 0

   Test: Integer_validator method with ValueError zero.
    >>> try:
    bg.integer_validator("x", 0)
    except Exception as err:
    print(err)
    x must be greater than 0

   Test: Integer_validator method with no arguments.
    >>> try:
    bg.integer_validator()
    except Exception as err:
    print(err)
    integer_validator() missing 2 required positional arguments: 'name' and 'value'

   Test: Integer_validator method with only one argument.
    >>> try:
    bg.integer_validator("x")
    except Exception as err:
    print(err)
    integer_validator() missing 1 required positional argument: 'value'

   Test: Integer_validator with None.
    >>> try:
    bg.integer_validator(None, None)
    except Exception as err:
    print(err)
    None must be an integer
