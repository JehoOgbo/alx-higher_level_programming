#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return a_dictionary
    if len(a_dictionary) == 0:
        return a_dictionary
    save = ""
    for k, v in a_dictionary.items():
        if v == value:
            save += k
            save += ' '
    length = len(save) - 1
    i = 0
    new = ''
    while i <= length:
        if save[i] != ' ':
            new += save[i]
        else:
            a_dictionary.pop(new)
            new = ''
        i += 1
    return (a_dictionary)
