#!/usr/bin/python3
"""Mylist list module"""


class MyList(list):
    """ a subclass MyList that inherits from list"""
    def print_sorted(self):
        number_sorted = []
        real_list = self
        for number in self:
            number_sorted.append(number)
        number_sorted.sort()
        print(number_sorted)
