#!/usr/bin/python3
"""
function that returns a
set of common elements in two sets.
"""


def common_elements(set_1, set_2):
    result = []
    len_1 = len(set_1)
    len_2 = len(set_2)
    if (len_1 <= len_2):
        for element in set_1:
            if element in set_2:
                result.append(element)
    elif (len_2 <= len_1):
        for element_2 in set_2:
            if element_2 in set_1:
                result.append(element_2)
    return (result)
