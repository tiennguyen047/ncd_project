import os
import sys
import numpy
import logging

def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def fibonacci_test(n):
    if n in [0, 1]:
        return n
    f_set = [0, 1]
    for i in range(n-1):
        a = f_set[0] + f_set[1]
        f_set[0] = f_set[1]
        f_set[1] = a
    return f_set[1]

if __name__ == "__main__":
    n = fibonacci_test(100000)