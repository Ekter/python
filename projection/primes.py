from time import time
import math
from numba import jit
import matplotlib.pyplot as plt
import numpy as np


@jit(nopython=True, nogil=True)
def premier(n:int)-> bool:
    if n==2 : return True
    if n % 2 == 0 or n <= 1: return False
    m=3
    r = math.sqrt(n)
    while m <= r:
        if n % m == 0:
            return False
        m += 2
    return n > 1

@jit(nopython=True, nogil=True)
def premier_list(n:int, lprimes : np.ndarray[int], count : int) -> bool:
    r = math.sqrt(n)
    for i in range(count):
        if n % lprimes[i] == 0:
            return False
        if lprimes[i] > r:
            return True
    return n>1

@jit(nopython=True, nogil=True)
def list_primes(size : int = 1000, method = premier) -> np.ndarray[int]:
    size2 = 2**size
    l = np.zeros(int(size2/math.log(2) + 10), dtype = np.uint64)
    count = 1
    l[0] = 2
    for i in range(3,size2,2):
        if method(i):
            l[count] = i
            count+=1
    return l

@jit(nopython=True, nogil=True)
def list_primes_2(size : int = 1000, method = premier_list) -> np.ndarray[int]:
    size2 = 2**size
    l = np.zeros(int(size2/math.log(2) + 10), dtype = np.uint64)
    count = 1
    l[0] = 2
    for i in range(3,size2,2):
        if method(i, l, count):
            l[count] = i
            count+=1
    return l

def plot_cylindrical_coords(l : np.ndarray[int]) -> None:
    plt.figure()
    plt.plot([i*math.cos(i) for i in l], [i*math.sin(i) for i in l], '.')
    plt.show()

number_it = 25
t = time()
l1=list_primes(number_it, premier)
print(time()-t)
t = time()
l1 = np.trim_zeros(l1)
print(time()-t)
print("-------------------------------")
# plot_cylindrical_coords(l)
print(l1)
t = time()
l2=list_primes_2(number_it)
print(time()-t)
t = time()
l2 = np.trim_zeros(l2)
print(time()-t)
# plot_cylindrical_coords(l)

assert np.all(l1==l2)
print(l1==l2)
print(np.trim_zeros(l1))
print(len(np.trim_zeros(l2)))
print(len(l2),len(l1))
