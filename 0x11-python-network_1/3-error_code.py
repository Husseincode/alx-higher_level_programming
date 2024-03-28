#!/usr/bin/python3
"""
   Python script that takes in a url
   sends a request to the URL and
   displays the body of the response (decoded in utf-8)
"""

from sys import argv
import urllib.request
import urllib.error


def main(url):
    """main function to execute the task"""
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main(argv[1])
