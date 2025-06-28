#!/usr/bin/python3
"""
Python script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
from requests import post


if __name__ == '__main__':
    try:
        q = argv[1]
    except IndexError:
        q = ''
    if len(q) > 1:
        q = ''
    response = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
