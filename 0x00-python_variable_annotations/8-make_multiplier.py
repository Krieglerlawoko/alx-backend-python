#!/usr/bin/env python3
"""Module for a function that creates a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiplier_func(num: float) -> float:
        """Multiplies a float by the given multiplier."""
        return num * multiplier
    return multiplier_func
