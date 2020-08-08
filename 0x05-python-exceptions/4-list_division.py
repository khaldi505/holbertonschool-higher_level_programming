#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    r = 0
    for x in range(list_length):
        try:
            r = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except TypeError:
            print("wrong type")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            result.append(r)
    return(result)
