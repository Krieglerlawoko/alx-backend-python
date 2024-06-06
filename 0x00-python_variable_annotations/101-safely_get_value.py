#!/usr/bin/env python3
"""Module for a function that safely retrieves a value from a dictionary."""

from typing import Mapping, Any, TypeVar, Union

# Define a TypeVar for the default value
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value associated with key in dct if it exists, otherwise returns the default value."""
    if key in dct:
        return dct[key]
    else:
        return default
