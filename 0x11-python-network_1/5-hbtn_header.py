#!/usr/bin/python3
"""
   a Python script that takes in a url:
   sends a request to the url
   and displays the value of the variable X-Display-Id
"""

import requests
from sys import argv


def main(url):
    """main function that executes the task"""
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main(argv[1])
