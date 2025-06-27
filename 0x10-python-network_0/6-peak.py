#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds the largest integer in the list """
    if list_of_integers is None or list_of_integers == []:
        return None
    save = 0
    for item in list_of_integers:
        if save < item:
            save = item
    return save
