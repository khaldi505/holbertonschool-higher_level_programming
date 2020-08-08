#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lenx = 0

    try:
        for lenx in range(x):
            print("{}".format(my_list[lenx]), end="")
            lenx += 1
    except:
        print("")
        return lenx
    else:
        print("")
        return lenx
