#!/usr/bin/python3
def delete_at(my_list=[], idx = 0):
    '''
    deletes the item at position idx in the list

    my_list: is the list containing items
    idx: index of object to be deleted
    Do not use pop()
    Do not import any module
    '''
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    del my_list[idx]
    return my_list
