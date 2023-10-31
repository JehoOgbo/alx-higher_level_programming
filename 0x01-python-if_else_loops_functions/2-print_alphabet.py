#!/usr/bin/python3


def print_low_alphabet():
    for character in range(97, 123):
        print('{}'.format(chr(character)), end='')


if __name__ == '__main__':
    print_low_alphabet()
