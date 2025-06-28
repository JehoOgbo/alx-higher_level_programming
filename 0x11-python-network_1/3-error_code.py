#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
from sys import argv
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request(argv[1])
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
    except urllib.error.URLError as e:
        print("Reason: ", e.reason)
    else:
        print(response.read().decode('utf-8'))
