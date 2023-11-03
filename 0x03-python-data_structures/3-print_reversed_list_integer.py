#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    print all integers of a list in reverse order

    print one integer per line
    my_list: the list whose elements of the future
    Assume list only contains integers
    Do not cast integers to strings
    You have to use str.format() to print integers
    '''
    if my_list is None:
        return
    length = len(my_list) - 1
    while length >= 0:
        print("{:d}".format(my_list[length]))
        length -= 1
