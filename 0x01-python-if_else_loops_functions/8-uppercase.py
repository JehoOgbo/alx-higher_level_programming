#!/usr/bin/python3


def uppercase(str):
    for character in str:
        newchar = ord(character)
        if newchar > 96 and newchar < 123:
            print('{}'.format(chr(newchar - 32), end=''))
        else:
            print('{}'.format(chr(newchar), end=''))
