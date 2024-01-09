#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8).

    :param filename: Name of the file to be written.
    :param text: String to be written to the file.
    :return: Number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters
