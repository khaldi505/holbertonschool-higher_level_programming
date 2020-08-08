#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        len_list = len(my_list)
        for x in range(len_list + 1):
            if x != 0:
                print("{:d}".format(my_list[-x]))
