#!/usr/bin/python3
"""
    Algoeithme that Find a peak of a list
"""


def find_peak(list_of_integers):
    """
        function that finds a peak in
        a list of unsorted integers.
    """

    lenList = len(list_of_integers)
    myList = list_of_integers

    if lenList == 0:
        return None
    elif lenList == 1:
        return myList[0]
    elif lenList == 2:
        return max(mylist)
    else:
        left = 0
        right = lenList - 1

        while left < right:
            mid = (left + right) // 2

            if myList[mid] < myList[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return myList[left]
