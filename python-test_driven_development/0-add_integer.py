#!/usr/bin/python3
"""This module provides a function to add two integers.

The function ensures inputs are integers or floats and returns
their sum as an integer.
"""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
