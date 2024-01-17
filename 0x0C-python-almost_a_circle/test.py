#!/usr/bin/python3

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1, 4, ok=7, lol=8)