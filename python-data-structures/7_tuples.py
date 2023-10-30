#!/usr/bin/python3
def tuple_addition(first_arg=(), second_arg=()):
    first = first_arg[:2]
    second = second_arg[:2]

    if len(first) < 2:
        first += (0,) * (2 - len(first))
    if len(second) < 2:
        second += (0,) * (2 - len(second))

    result = (first[0] + second[0], first[1] + second[1])
    return result
