#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''
    prints a matrix of integers

    matrix: integer matrix to be printed

    Do not import any module
    Assume the list only contains integers
    Do not cast integers into strings
    Use str.format() to print integers
    '''
    if matrix == [[]]:
        print("")
    for i in matrix:
        k = 0
        while k < len(i) - 1:
            print("{:d}".format(i[k]), end=' ')
            k += 1
        if i:
            print("{:d}".format(i[k]))
