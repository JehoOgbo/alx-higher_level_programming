#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list like in c

    my_list: the list from which the element is to be removed
    idx: index of element to be removed

    If idx is negative return None
    If idx is out of range return None
    Do not import any module
    Do not use try or except
    """
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    return (my_list[idx])
