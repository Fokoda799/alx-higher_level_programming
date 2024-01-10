#!/usr/bin/python3
""" My List Module """

class MyList(list):
    """My List Obj
       inherits from: List obj"""

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """ Function that print,
            sorted list"""

        sortedList = sorted(self)
        print (f"{sortedList}")
