#!/usr/bin/python3


def print_comb3():
    for num in range(0, 9):
        for new in range(1, 10):
            if (num != new and num < new and num != 8):
                print('{}{}'.format(num, new), end=', ')
    print('{}'.format(89))


if __name__ == '__main__':
    print_comb3()
