#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return(my_list)
    else:
        for x in range(0, len(my_list)):
            if x == idx:
                my_list.remove(my_list[x])
    return(my_list)
