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
    if type(roman_string) is not str:
        return 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    num['D'] = 500
    num['M'] = 1000
    last = 0
    number = 0
    for i in reversed(roman_string):
        if i in num:
            if num[i] >= last:
                last = num[i]
                number += last
            else:
                last = num[i]
                number -= last
        else:
            print("Not a roman Numeral")
            return 0
    return number
