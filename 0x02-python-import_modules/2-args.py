#!/usr/bin/python3
if __name__ ==  "__main__":
    import sys

    args = sys.argv[1:]
    i = len(args)
    x = 0

    if i > 1:
        print("{} arguments:".format(i))
        for j in range(i):
            x +=1
            print("{}: {}".format(x, args[j]))
    else:
        print("0 argument.")
