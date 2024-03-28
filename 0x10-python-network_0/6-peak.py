#!/usr/bin/python3
""" An algorithm that finds a peak
from an unsorted list of integers """


def find_peak(list_of_integers):
    """ function that finds a peak in a list of
    unsorted integers.
    Args:
        list_of_integers: list[int].
    Return: returns the peak."""
    _len = len(list_of_integers)
    if _len == 0:
        return None
    if _len == 1:
        return list_of_integers[0]

    left = 0
    right = _len - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
