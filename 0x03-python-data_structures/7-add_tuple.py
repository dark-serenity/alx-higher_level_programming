#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = tuple_a + tuple_b

    if result < 2:
        print('0')
    elif result > 2:
        print("{:2}".format(result))
