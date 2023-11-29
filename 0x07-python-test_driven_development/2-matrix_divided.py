#!/usr/bin/python3

"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of the matrix by a number
    Args:
        matrix: matrix containing lists of integers or floats
        div: divisor to be used to divide all the elements of the matrix
    Raises a TypeError if a member of a list of matrix is not an int or float
    Raises a TypeError if all rows of the matrix are not the same size
    Raises a TypeError if div is not an int or float
    Raise a ZeroDivisionError if div is Zero
    Divide all elements by div rounded to 2 decimal places

    Returns a new matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by Zero")
    i = 0
    length = len(matrix)
    while i < length:
        if i != length - 1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
        for element in matrix[i]:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
        i += 1
    new = []
    for i in matrix:
        new.append(list(map(lambda x: round(x / div, 2), i)))
    return new
