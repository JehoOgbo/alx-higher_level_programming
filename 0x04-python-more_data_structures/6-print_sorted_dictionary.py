#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
    Prints a dictionary by ordered keys
    Assume all keys are strings

    Keys should be sorted in alphabetic order
    Only sort keys inside the main dictionary
    Dictionary values can have any type
    You are not allowed to import any module
    return None
    '''
    if a_dictionary is None:
        print(None)
    for k, v in sorted(a_dictionary.items()):
        print("{:s}: {}".format(k, v))
