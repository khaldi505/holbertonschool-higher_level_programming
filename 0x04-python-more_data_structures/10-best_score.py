#!/usr/bin/python3
def best_score(a_dictionary):
    value = 0
    key = ""
    if a_dictionary is None or a_dictionary == {}:
        return None
    for k, v in a_dictionary.items():
        if a_dictionary[k] > value:
            key = k
            value = a_dictionary[k]
    return key
