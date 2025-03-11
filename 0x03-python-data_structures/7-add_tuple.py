#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    adds two tuples

    returns a new tuple with two integers
    Do not import any module
    Assume that the tuples will contain integers
    If a tuple is smaller than 2 use 0 for each missing integer
    If a tuple is bigger than 2, use only the first two integers
    '''
    length = len(tuple_a)
    if length > 1:
        a = tuple_a[0]
        b = tuple_a[1]
    elif length == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = 0
        b = 0
    length = len(tuple_b)
    if length > 1:
        c = tuple_b[0]
        d = tuple_b[1]
    elif length == 1:
        c = tuple_b[0]
        d = 0
    else:
        c = 0
        d = 0
    num1 = a + c
    num2 = b + d
    new = num1, num2
    return new
