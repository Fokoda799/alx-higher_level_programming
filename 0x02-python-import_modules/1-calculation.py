#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5
op = ["+", "-", "*", "/"]

for o in op:
    if o == "+":
        r = add(a, b)
    elif o == "-":
        r = sub(a, b)
    elif o == "*":
        r = mul(a, b)
    else:
        r = div(a, b)

    print("{} {} {} = {}".format(a, o, b, r))
