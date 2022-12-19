#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists
    the lists can contain any type
    list_length can be bigger than the length of both lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements can't be divided, the result should be 0
    If an element is not int or float print wrong type
    if the division cant be done, print division by 0
    If my_list_1 or my_list_2 is too short, print out of range
    Use try: / except: / finally:
    Do not import any module
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
