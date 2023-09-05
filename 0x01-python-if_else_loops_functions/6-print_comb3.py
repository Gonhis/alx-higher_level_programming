#!/usr/bin/python3
for DG1 in range(10):
    for DG2 in range(DG1 + 1, 10):
        if DG1 == 0 and DG2 == 1:
            print("01", end=", ")
        else:
            print("{:02}".format(DG1 * 10 + DG2), end=", ")
