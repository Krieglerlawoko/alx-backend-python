#!/usr/bin/env python3
"""Module for a function that zooms in on an array."""


from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """Returns a zoomed-in version of the input array."""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Change to tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Change factor to integer
