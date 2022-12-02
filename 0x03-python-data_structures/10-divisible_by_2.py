#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    finds all multiples of two in a list

    Return a list with true or false according to index and truth value
    The new list should have the same size as the original list
    Do not import any module
    """
    if len(my_list) == 0:
        return False
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
