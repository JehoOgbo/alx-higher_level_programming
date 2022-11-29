#!/usr/bin/python3

# fizzbuzz - prints 1 to 100 separated by space
# if the number is a multiple of 3 print Fizz
# if it's a multiple of 5 print Buzz
# if it's a multiple of 15 print FizzBuzz
# you're not allowed to import any module

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
