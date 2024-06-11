#!/usr/bin/env python3
"""measure_runtime"""

import asyncio
from time import time
from 1_async_comprehension import async_comprehension


async def measure_runtime():
    """Measure the total runtime of running async_comprehension four times in parallel."""
    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time()
    return end_time - start_time
