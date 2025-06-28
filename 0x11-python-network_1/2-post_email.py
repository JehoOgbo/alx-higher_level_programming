#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == '__main__':
    data = {
            'email': argv[2]
    }
    encoded = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(argv[1], data=encoded)

    with urllib.request.urlopen(request) as response:
        variable = response.read().decode('utf-8')

    print(variable)
