#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response.
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    response = get(argv[1])
    if response.status_code == 200:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
