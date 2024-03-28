#!/usr/bin/python3
"""
   a Python script that takes in a url:
   and post an email to  the url
   and displays the body of the content of the response
"""

import requests
from sys import argv


def main(url):
    """main function that executes the task"""
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)


if __name__ == "__main__":
    main(argv[1])
