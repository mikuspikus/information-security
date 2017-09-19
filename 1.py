import math as mth
from functools import reduce
from operator import add
import time

#sieve of Eratosthenes
def erectum_sten(n):
    a = [True] * (n + 1)
    for i in range(2, int(mth.sqrt(n))):
        for j in range(i * 2, n, i):
            a[j] = False
    return [i for i in range(2, n) if a[i]]

#trial division
def prime_trial(k):
    for i in erectum_sten(int(mth.sqrt(k))):
        if k % i == 0:
            return i
    return 0

k = 1000190
print('Trial division for k = {0}'.format(k))
if prime_trial(k):
    print('\tNot prime! Divided by {0}'.format(prime_trial(k)))
else:
    print('\tPrime!')
                    

# pi
def pi_lagr(k):
    n = erectum_sten(k)[-1]
    return n / (mth.log(n, mth.e) - 1.08633)

def pi_modern_lagr(k):
    n = erectum_sten(k)[-1]
    return n / (mth.log(n, mth.e) - (1 - (n * mth.log(n, mth.e)) ** (-1) 
                                     - reduce(add, [mth.log(n, mth.e) ** -i for i in range(1, k)])))

def pi_hadamard(k):
    n = erectum_sten(k)[-1]
    return n / mth.log(n, mth.e)

print('\nLagrange formula: {0:.4f}'.format(pi_lagr(k)))
print('Modified Lagrange formula: {0:.4f}'.format(pi_modern_lagr(k)))
print('Hadamard formula: {0:.4f}'.format(pi_hadamard(k)))
print(erectum_sten(1000))