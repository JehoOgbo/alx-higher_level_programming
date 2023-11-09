#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix

    matrix is a two dimensional array

    Returns a new matrix same size as original with values square of input
    Do not modify the initial matrix
    Do not import any module
    You can use regular loops, map, etc
    """
    if matrix is None:
        return matrix
    if matrix is [[]]:
        return matrix
    new = [a[:] for a in matrix]
    len1 = len(matrix)
    for i in range(len1):
        len2 = len(matrix[i])
        for j in range(len2):
            new[i][j] = matrix[i][j] ** 2
    return (new)
