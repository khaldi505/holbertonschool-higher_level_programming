#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    b0 = 0
    b1 = 0
    a1 = 0
    a0 = 0
    if len(tuple_b) - 1 == 0:
        b0 = int(tuple_b[0])
    elif len(tuple_b) >= 2:
        b1 = tuple_b[1]
        b0 = tuple_b[0]
    if len(tuple_a) - 1 == 0:
        a0 = tuple_a[0]
    elif len(tuple_a) >= 2:
        a1 = tuple_a[1]
        a0 = tuple_a[0]

    resulta = b0 + a0
    resultb = b1 + a1
    tuple_result = (resulta, resultb)
    return(tuple_result)
