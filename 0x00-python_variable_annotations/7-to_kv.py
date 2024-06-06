#!/usr/bin/env python3
"""Module for a function to create a tuple with a string and the square of an int or float."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of the int/float v."""
    return (k, v ** 2)
