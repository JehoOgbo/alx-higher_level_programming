#!/usr/bin/python3
def multiple_returns(sentence):
    """
    return a tuple with the length of a string and its first character

    sentence: string to be used for tuple creation
    if sentence is empty then the first char should be equal to None
    Do not import any module
    """
    length = len(sentence)
    if length == 0:
        new = length, None
        return new
    char = sentence[:1]
    new = length, char
    return new
