import numpy as np
import math

"""
Sieve(n) provides a list called primes with all the prime numbers up to and
including n
input: integer n
output: list
"""
def sieve(n):
    binary = np.zeros([n+1])  # May need to include dtype = np.dtype('f4'))
    for i in range (2,n+1):
        binary[i] = 1
    p = 2
    while pow(p,2)<=n+1:
        j = p+p
        while j<=n:
            binary[j] = 0
            j = j+p
        p = p+1
        while binary[p]==0:
            p=p+1
    primes = []
    primes.append(2)
    for p in range (3,n):
        if binary[p]==1:
            primes.append(p)
    return primes
