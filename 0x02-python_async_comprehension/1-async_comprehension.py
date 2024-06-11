#!/usr/bin/env python3
"""
Coroutine that collects 10 random
numbers using async comprehensions.
"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async
    comprehensions over async_generator.
    """
    return [i async for i in async_generator()]
