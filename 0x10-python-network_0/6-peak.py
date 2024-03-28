#!/usr/bin/python3
""" An algorithm that finds a peak
    from an unsorted list of 
    integers """


def find_peak(list_of_integers):
    """ function that finds a peak in
    a list of unsorted integers.
    Args:
        list_of_integers: list[int].
    Return: returns the peak.
    """
    _len = len(list_of_integers)
    myList = list_of_integers

    if _len == 0:
        return None
    if _len == 1:
        return myList[0]

    for i in range(1, _len):
        j = i - 1
        k = i + 1
        if k == _len:
            break
        p = myList[i]
        if p > myList[j] and p > myList[k]:
            return myList[i]
    return max(myList)
