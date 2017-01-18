# File timer.py
"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
"""

import time, sys
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else: timer = time.clock if sys.platform[:3] == 'win' else time.time()

def total(func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32 # 136 years seem large enough
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))

