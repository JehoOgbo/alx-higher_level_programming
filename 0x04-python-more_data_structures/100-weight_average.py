#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple
    Data is a list of two element tuples

    Return: 0 if list is empty
    Do not import any module
    """
    if my_list is None:
        return 0
    if len(my_list) == 0:
        return 0
    product = 0
    divisor = 0
    for i in my_list:
        product += i[0] * i[1]
        divisor += i[1]
    return product / divisor
