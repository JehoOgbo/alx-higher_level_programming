#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the
GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    author = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=author)
    print(r.json().get("id"))
