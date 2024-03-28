#!/usr/bin/python3
"""
   a Python script that fetches:
   https://alx-intranet.hbtn.io/status
"""

import requests


def main():
    """main function that executes the task"""
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")


if __name__ == "__main__":
    main()
