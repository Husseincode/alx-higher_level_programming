#!/usr/bin/python3

"""
    Inserts a line of text after each line containing a specific string in the file.

    :param filename: Name of the file.
    :param search_string: String to search for in each line.
    :param new_string: String to be inserted after each line containing the search_string.
"""


def append_after(filename="", search_istring="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in the file.

    :param filename: Name of the file.
    :param search_string: String to search for in each line.
    :param new_string: String to be inserted after each line containing the search_string.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, mode="w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
