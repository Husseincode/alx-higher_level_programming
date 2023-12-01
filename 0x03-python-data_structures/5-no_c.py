#!/usr/bin/python3
def no_c(my_string):
    modified_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            modified_string += i
    return modified_string
