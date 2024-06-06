#!/usr/bin/env python3
"""Module for a function that safely retrieves the first element of a list."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """first element of list if it exists, else None."""
    if lst:
        return lst[0]
    else:
        return None
