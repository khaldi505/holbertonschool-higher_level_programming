#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    def div(x, y): return x / y

    def sum(x, y): return x + y

    def mul(x, y): return x * y
    the_other_side = 0
    result = 0
    for element in my_list:
        for tupo in range(0, len(element), 2):
            result += element[tupo] * element[tupo + 1]
            the_other_side += element[tupo + 1]
    return div(result, the_other_side)
