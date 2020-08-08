#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(0, len(my_list)):
        if idx == x:
            return my_list[x]
        elif idx < 0 or idx > len(my_list):
            return None
