#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    replaces all occrences of an element by another in a new list
    my_list: is the initial list

    search is the element to replace in the list
    replace is the new element
    You are not allowed to import any module
    '''
    if my_list is None:
        return my_list
    if my_list is []:
        return my_list
    new = my_list[:]
    length = len(my_list)
    for i in range(length):
        if new[i] == search:
            new[i] = replace
    return new
