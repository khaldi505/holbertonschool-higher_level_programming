#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = 0
    list_len = len(my_list) - 1
    new_list = my_list.copy()
    if idx < 0 or list_len < idx:
        return my_list
    if idx >= 0 or idx < list_len:
        new_list.remove(idx + 1)
        new_list.insert(idx, element)
        return new_list
