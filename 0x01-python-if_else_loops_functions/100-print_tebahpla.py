#!/usr/bin/python3


def tebalpha():
    i = 122
    while i > 96:
        if i % 2 == 0:
            print('{}'.format(chr(i)), end='')
        else:
            print('{}'.format(chr(i - 32)), end='')
        i = i - 1


if __name__ == '__main__':
    tebalpha()
