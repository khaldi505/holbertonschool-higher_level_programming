#!/usr/bin/python3
'''
a function that replaces all
occurrences of an element by another in a new list.
'''


def search_replace(my_list, search, replace):
    my_new_list = []
    for element in my_list:
        if (search == element):
            my_new_list.append(replace)
        else:
            my_new_list.append(element)
    return my_new_list
