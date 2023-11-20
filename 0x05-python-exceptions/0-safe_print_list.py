#!/usr/bin/python3

# prints x elemebts of a list

def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]))
        except IndexError:
            print("Index does not exist")
        i += 1
    return i
