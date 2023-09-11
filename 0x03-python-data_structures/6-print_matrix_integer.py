#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ism in matrix:
        for hid in ism:
            print("{:d}".format(hid), end=" " if hid != ism[-1] else "")
        print()
