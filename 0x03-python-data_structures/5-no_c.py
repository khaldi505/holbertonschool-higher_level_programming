#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    strlen = len(my_string)
    for x in range(strlen):
        if my_string[x] != 'c':
            if my_string[x] != 'C':
                new_string += my_string[x]
    return new_string
