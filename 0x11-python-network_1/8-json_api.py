#!/usr/bin/python3
"""
   a Python script that takes in a url:
   and post a leter to  the url as a search param
   and displays the body of the content of the response
"""


import requests
from sys import argv


def main(letter=""):
    """main function that executes the task"""
    params = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=params)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(argv) >= 2:
        main(letter=argv[1])
    else:
        main()
