def fac_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fac_recursive(n-1)

def fac_reduce(n):
    from functools import reduce
    if n==0: return 1
    return reduce(lambda x, y: x * y, range(1, n+1))

def fac_loop(n):
    if n==0: return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fac_mathfac(n):
    from math import factorial
    return factorial(n)

