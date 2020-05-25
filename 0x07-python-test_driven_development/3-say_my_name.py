#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first_name> <last_name>
    Parameters:
        first_name: must be strings
        last_name: must be strings
    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))