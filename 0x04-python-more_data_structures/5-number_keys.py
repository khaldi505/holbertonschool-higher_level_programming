#!/usr/bin/python3
"""
a function that returns the
number of keys in a dictionary.
"""


def number_keys(a_dictionary):
    result = 0
    for key in a_dictionary.items():
        result += 1
    return result
