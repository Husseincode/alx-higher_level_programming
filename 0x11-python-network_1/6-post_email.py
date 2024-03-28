#!/usr/bin/python3
"""
   a Python script that takes in a url:
   and post an email to  the url
   and displays the value of the content of the response
"""

import requests
from sys import argv


def main(url, email):
    """main function that executes the task"""
    email = {'email': email}
    r = requests.post(url, data=email)
    print(r.text)


if __name__ == "__main__":
    main(argv[1], argv[2])
