#!/usr/bin/env python3
"""Coroutine to measure runtime of async comprehensions."""

import asyncio
from time import perf_counter
from 1-async_comprehension import async_comprehension


async def measure_runtime():
    """Measure  total runtime of running
    async_comprehension four times in parallel."""
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in 4))
    end_time = perf_counter()
    return end_time - start_time
