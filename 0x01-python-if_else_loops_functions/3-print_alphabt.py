#!/usr/bin/python3


def print_low_alphabt():
    for character in range(97, 123):
        if character != 101 and character != 113:
            print('{}'.format(chr(character)), end='')


if __name__ == '__main__':
    print_low_alphabt()
