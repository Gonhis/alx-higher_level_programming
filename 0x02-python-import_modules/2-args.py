#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1
    if index == 0:
        print("0 arguments.")
    elif index == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(index))
    for c in range(index):
        print("{}: {}".format(c + 1, sys.argv[c + 1]))
