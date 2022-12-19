#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x elements of the list my_list
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    You have to use try: / except:
    Do not import any module
    Do not use len()
    """
    try:
        i = 0
        while i < x:
            print("{}".format(my_list[i]), end='')
            i += 1
    except IndexError:
        print('')
        return i
    else:
        print('')
        return i
