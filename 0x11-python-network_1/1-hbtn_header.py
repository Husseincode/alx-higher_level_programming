#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
"""
import urllib.request
import sys


def main(url):
    """ function to print a header of a url """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.getheader('X-Request-Id'))


if __name__ == "__main__":
    main(sys.argv[1])
