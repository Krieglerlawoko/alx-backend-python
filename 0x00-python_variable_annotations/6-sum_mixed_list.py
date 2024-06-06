#!/usr/bin/env python3
"""Module for a function that sums a mixed list of integers and floats."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a mixed list of integers and floats."""
    return sum(mxd_lst)
