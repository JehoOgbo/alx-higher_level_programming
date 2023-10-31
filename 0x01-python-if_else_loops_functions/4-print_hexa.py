#!/usr/bin/python3


def print_hexa():
    for num in range(0, 99):
        print('{} = 0x{:x}'.format(num, num))


if __name__ == '__main__':
    print_hexa()
