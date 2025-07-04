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
                                                              argv[2],
                                                              argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
