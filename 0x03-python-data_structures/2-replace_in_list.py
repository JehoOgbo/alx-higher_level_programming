#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific location (like in C)

    my_list: list which is to be manipulated
    idx: index which is to be changed
    element: the new element of the list

    If idx if negative return original list
    If idx is out of range, return original list
    Do not use try/except
    """
    if my_list is None:
        return my_list
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
