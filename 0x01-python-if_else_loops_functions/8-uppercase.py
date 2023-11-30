#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            code = ord(c) - 32
        else:
            code = ord(c)
        print(f"{code :c}", end="")
    print("")
