#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets

    set_1: 1st set
    set_2: 2nd set
    Do not import any module
    """
    if set_1 is None or set_2 is None:
        return None
    return (set_1 & set_2)
