#!/usr/bin/python3
"""
function that returns a set of
all elements present in only one set.
"""


def only_diff_elements(set_1, set_2):
    result = []
    for element in set_1:
        if element in set_2:
            pass
        else:
            result.append(element)
    for element_2 in set_2:
        if element_2 in set_1:
            pass
        else:
            result.append(element_2)
    return (result)
