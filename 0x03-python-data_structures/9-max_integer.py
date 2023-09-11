#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    maxum = my_list[0]
    for c in range(len(my_list)):
        if my_list[c] > maxum:
            maxum = my_list[c]
    return (maxum)
