#!/usr/bin/python3

def remove_char_at(str, n):
    j = 0
    chars = ""
    for i in str:
        if j != n:
            chars = chars + i
        j = j + 1
    return (chars)
