#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition = 0
    for c in range(len(sys.argv) - 1):
        addition += int(sys.argv[c + 1])
    print("{}".format(addition))
