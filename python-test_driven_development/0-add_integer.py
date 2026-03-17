#!/usr/bin/python3
"""
Module 0-add_integer
This module contains a function that adds two integers.
Floats are casted to integers. TypeError is raised if the arguments
are not integers or floats, or if the float is NaN/inf.
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result.

    Args:
        a (int/float): first number
        b (int/float, optional): second number, default is 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not int/float or float NaN/inf
    """
    import math  # yalnız NaN/inf yoxlamaq üçün, normal əlavə etməyə icazə verilir

    # Type check
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN / inf yoxlama
    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise TypeError("cannot convert float NaN to integer")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise TypeError("cannot convert float NaN to integer")

    # Convert to integer
    a_int = int(a)
    b_int = int(b)

    return a_int + b_int
