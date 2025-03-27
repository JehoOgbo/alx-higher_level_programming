#!/usr/bin/python3

"""Function that adds two values."""


def add_integer(a, b=98):
    """ adds two given values
        Args:
            a - numeric data which must be provided
            b - numeric data which defaults to 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
