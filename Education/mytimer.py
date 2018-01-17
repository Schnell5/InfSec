"""
Counting the time on the function
"""

import time

reps = 10000
replist = range(reps)


def timer(func, *args, **kwargs):
    start = time.clock()
    for _ in replist:
        ret = func(*args, *kwargs)
    elapsed = time.clock() - start

    return elapsed, ret



