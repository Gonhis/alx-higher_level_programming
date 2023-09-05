#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
DG = abs(number) % 10
if number < 0:
    DG = -DG
print("Last digit of {} is {} and is ".format(number, DG), end="")
if DG > 5:
    print("greater than 5")
elif DG == 0:
    print("0")
else:
    print("less than 6 and not 0")
