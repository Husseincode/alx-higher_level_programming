#!/usr/bin/python3
"""
   a Python script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import sys
import urllib.request


def main(url, email):
    """Function to post email and print the response body"""
    email = {'email': email}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        the_page = res.read().decode('utf-8')
    print(the_page)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
