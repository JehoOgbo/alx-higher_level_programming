#!/usr/bin/python3


def print_last_digit(number):
    store = number % 10
    if number < 0:
        store = 10 - store
    print('{}'.format(store), end='')
    return (store)
