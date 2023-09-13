#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    alph_ord = list(a_dictionary.keys())
    alph_ord.sort()
    for i in alph_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
