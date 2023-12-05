#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    new_list = []
    for i in range(len(my_list)-1):
        if idx == i:
         new_list.append(element)
        new_list.append(my_list[i])
    return new_list
