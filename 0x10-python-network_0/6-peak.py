#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds the largest integer in the list """
    if list_of_integers is None or list_of_integers == []:
        return None
    i = 0
    save = 0
    try:
        while list_of_integers[i]:
            if save < list_of_integers[i]:
                save = list_of_integers[i]
            if save < list_of_integers[i + 1]:
                save = list_of_integers[i + 1]
            i += 2
    except IndexError:
        return save
