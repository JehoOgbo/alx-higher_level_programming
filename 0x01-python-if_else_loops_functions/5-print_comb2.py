#!/usr/bin/python3


def print_comb():
    for num in range(0, 99):
        print('{:02}'.format(num), end=', ')
    print('{}'.format(99))


if __name__ == '__main__':
    print_comb()
