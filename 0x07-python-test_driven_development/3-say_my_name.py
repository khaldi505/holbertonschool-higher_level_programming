#!/usr/bin/python3
"""
Prints last and firstname in a sentence
first_name = str
last_name = str
"""


def say_my_name(first_name, last_name=""):
    """ a function that prints My name is <first name> <last name> """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
