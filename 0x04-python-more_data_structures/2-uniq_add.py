#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_list = []

    def sum(number): return number + number
    for number in my_list:
        if number in new_list:
            pass
        else:
            new_list.append(number)
    for x in new_list:
        result += x
    return result
