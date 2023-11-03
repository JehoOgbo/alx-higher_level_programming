#!/usr/bin/python3
def no_c(my_string):
    """
    removes all characters c and C from a string

    my_string: string from which the above are to be removed
    Return: the new string

    Do not import any module
    You are not allowed to use str.replace()
    """
    new = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            new = new + i
    return new
