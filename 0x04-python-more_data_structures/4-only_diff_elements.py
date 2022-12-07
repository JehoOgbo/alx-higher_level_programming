#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''
    Returns a set of elements present in only one set
    That is only elements which are not present in both sets
    '''
    return (set_1 ^ set_2)
