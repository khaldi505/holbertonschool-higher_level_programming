#!/usr/bin/python3
"""
function that replaces or adds
key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value

    for k, v in a_dictionary.items():
        if key == k:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value

    return a_dictionary
