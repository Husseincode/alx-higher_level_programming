#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API
    to display your id
"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth


def main(username, passwd):
    """function to perform the task"""
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, passwd)
    r = requests.get(url, auth=auth)
    print(r.json().get("id"))


if __name__ == "__main__":
    main(argv[1], argv[2])
