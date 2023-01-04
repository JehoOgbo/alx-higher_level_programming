#!/usr/bin/python3

"""Function that adds two values."""


def add_integer(a, b=98):
    """Computes the sum of a and b
    a and b must be integers or floats
    Function works even if b is not provided as it has an arbitrary value
    Float arguments are typecasted to ints before addition takes place
    Raise:
        TypeError if either a or b is not an integer or float
    Return: the sum of the two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
