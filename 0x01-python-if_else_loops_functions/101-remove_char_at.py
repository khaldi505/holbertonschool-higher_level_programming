#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for x in range(0, len(str)):
        if x != n:
            new_str += str[x]
    return(new_str)
