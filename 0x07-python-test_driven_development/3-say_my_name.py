#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """function that prints:
      My name is <first name> <last name>"""

    e = "first_name must be a string or last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(e)
    if not isinstance(last_name, str):
        raise TypeError(e)

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("3-say_my_name.txt")
