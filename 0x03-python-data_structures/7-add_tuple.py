#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        length_of_a = (2 - len(tuple_a))
        if length_of_a == 1:
            tuple_a += (0,)
        else:
            tuple_a += (0, 0)
    if len(tuple_b) < 2:
        length_of_b = (2 - len(tuple_b))
        if length_of_b == 1:
            tuple_b += (0,)
        else:
            tuple_b += (0, 0)
    result = ()
    result += (tuple_a[0] + tuple_b[0],)
    result += (tuple_a[1] + tuple_b[1],)
    return (result)
