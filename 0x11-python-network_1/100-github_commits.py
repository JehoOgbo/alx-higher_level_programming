#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
                                                              sys.argv[2],
                                                              sys.argv[1])
    author = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                                  commits[i].get("sha"),
                                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
