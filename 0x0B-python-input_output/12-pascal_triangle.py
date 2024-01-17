#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    if n <= 0:
        return []

    My_list = []
    sub_list = []
    for i in range(n):
        for j in range(i + 1):
            sub_list.append(j)
        My_list.append(sub_list)
        sub_list.clear
    return My_list