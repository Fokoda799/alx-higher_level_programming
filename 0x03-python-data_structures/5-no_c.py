#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i, str in emunerate(my_string, start= 0):
         if str == "c" or str == "C":
             continue
	new_string[i] = str
    return new_string
