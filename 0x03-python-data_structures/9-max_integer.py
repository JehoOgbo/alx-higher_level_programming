#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
    finds the biggest integer of a list

    if the list is empty return None
    Assume list only contains integers
    Do not import any module
    Do not use the builtin max()
    '''
    length = len(my_list)
    if length == 0:
        return None
    i = 0
    maximum = my_list[0]
    while i < length:
        if maximum < my_list[i]:
            maximum = my_list[i]
        i += 1
    return maximum
