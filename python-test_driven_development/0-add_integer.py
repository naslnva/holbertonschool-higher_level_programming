#!/usr/bin/python3
"""
0-add_integer module
Contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Args:
        a (int/float): first number
        b (int/float, optional): second number (default 98)

    Raises:
        TypeError: if a or b is not an integer or float
        ValueError: if a or b is NaN or infinity

    Returns:
        int: sum of a and b
    """
    # Type checking
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN or Infinity
    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")
    if a == float("inf") or a == float("-inf") or b == float("inf") or b == float("-inf"):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
