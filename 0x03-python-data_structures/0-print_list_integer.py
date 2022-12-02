#!/usr/bin/python3
def print_list_integer(mylist=[]):
    """
    Prints all integers of a list

    One integer per line
    Do not import any module
    Assume the list only contains integers
    Do not cast integers into strings
    Use str.format() to print integers
    """
    for i in mylist:
        print("{:d}".format(i))
