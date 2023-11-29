#!/usr/bin/python3

def print_square(size):
    """Prints a square with a given size
    Args:
        size: length of a side of the square
    Raise a typeError if size is not an integer
    Raise a ValueError if it is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print('#', end='')
            j += 1
        print("")
        i += 1
