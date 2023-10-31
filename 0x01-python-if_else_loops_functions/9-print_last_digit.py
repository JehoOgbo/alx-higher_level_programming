#!/usr/bin/python3


def print_last_digit(number):
    store = number % 10
    print('{}'.format(store), end='')
    return (store)
