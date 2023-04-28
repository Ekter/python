
import numpy as np
from numba import jit
import math


@jit(nopython=True, nogil=True)
def decompose(n : np.uint16):
    NUMBER = 8 if n%10 != 0 else 11
    for i in range(1,10000):
        if NUMBER**i%n == 1:
            print(i)
            print((NUMBER**(i/2)+1)*(NUMBER**(i/2)-1))
            return  math.gcd(NUMBER**(i/2)+1,n)










print(decompose(37*5))