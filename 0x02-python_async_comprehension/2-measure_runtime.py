#!/usr/bin/env python3
"""
Measure runtime of executing
async comprehensions in parallel.
"""

import asyncio
from time import perf_counter
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times
    in parallel and measure the total runtime.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    return end_time - start_time
