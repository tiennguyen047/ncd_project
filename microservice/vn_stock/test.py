import unittest
from math import sqrt
def pFactors(n):
    """Finds the prime factors of 'n'"""
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    if n == 1: return [1]
    for check in range(2, limit):
            while num % check == 0:
                pFact.append(check)
                num /= check
    if num > 1:
        pFact.append(num)
    return pFact

for i in range(2,1000):
    print(pFactors(i))


