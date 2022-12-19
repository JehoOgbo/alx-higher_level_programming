#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers
    my_list can contain any type
    All integers to be printed on same line followed by a new line
    x is num of elements to access in my_list and can be bigger than list len
    Returns the real number of integers printed
    Use try: / except:
    Use str.format for integer printing
    Do not import any module
    Do not use len()
    """
    try:
        i = 0
        count = 0
        while i < x:
            if type(my_list[i]) is not int:
                i += 1
            if i < x:
                print("{:d}".format(my_list[i]), end='')
                i += 1
                count += 1
    except ValueError:
        print("")
        return count
    else:
        print("")
        return count
