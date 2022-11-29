#!/usr/bin/python3
# print the last digit of a number; returns last digit
def print_last_digit(number):
    if number == 0:
        print(0, end="")
        return (0)
    if (number < 0):
        print(-number % 10, end='')
        return (-number % 10)
    else:
        print(number % 10, end='')
        return (number % 10)
