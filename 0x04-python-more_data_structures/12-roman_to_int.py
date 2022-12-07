#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a roman numeral to an integer
    Assume the number will be between 1 to 3999

    Returns an integer
    Ef argument is not a string or None, return 0
    """
    if roman_string is None:
        return 0
    if roman_string is not str:
        return 0
