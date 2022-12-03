#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
    replaces an element in a list at an index without modifying the original
    my_list: list to be used as original
    idx: index of new list to be replaced
    element: element to be used for replacement

    Do not import any module
    Do not use try/except
    '''
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    new = my_list[:]
    new[idx] = element
    return new
