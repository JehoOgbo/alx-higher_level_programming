#!/usr/bin/python3
# print ascii alphabets in lowercase not followed by newline without q and e
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end='')
