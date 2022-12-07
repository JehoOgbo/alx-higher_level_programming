#!/usr/bin/python3
def best_score(a_dictionary):
    '''
    finds the key with the biggest integer value
    Assume all values are integers
    If no score is found return None
    Assume all students have a different score

    Do not import any module
    '''
    if a_dictionary is None:
        return (None)
    if len(a_dictionary) == 0:
        return (None)
    old = 0
    for k, v in a_dictionary.items():
        if v > old:
            save = k
            old = v
    return save
