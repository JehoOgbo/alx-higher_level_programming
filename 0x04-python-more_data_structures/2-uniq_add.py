#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer)

    my_list: list whose elements are to be added
    return the result of the addition
    """
    if my_list is None:
        return 0
    if my_list is []:
        return 0
    new = set(my_list)
    summer = 0
    for i in new:
        summer += i
    return summer
