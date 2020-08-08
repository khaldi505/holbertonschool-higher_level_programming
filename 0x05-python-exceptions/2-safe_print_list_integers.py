#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 1
    try:
        for y in range(0, x):
            if type(my_list[y]) == int:
                print("{:d}".format(count), end="")
                count += 1
        print()
        return count - 1
    except:
        pass
