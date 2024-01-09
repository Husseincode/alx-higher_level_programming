#!/usr/bin/python3
def read_file(filename=""):
    """
    Read the content of a UTF-8 encoded text file and print it to stdout.
    :param filename: Name of the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
