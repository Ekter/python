import time
from numba import jit
import numpy as np

SIZE = 1000

@jit(nopython=True, nogil=True)
def orthonormize(l : np.ndarray[np.float64]) -> np.ndarray[np.float64]:
    l[0] /= np.linalg.norm(l[0])
    i=1
    for i in range(1,len(l)):
        for j in range(i):
            l[i] -= l[j].dot(l[i])*l[j]
        l[i] /= np.linalg.norm(l[i])
    return l

a = np.random.normal(size=(SIZE, SIZE))

print(a)
t = time.time()
print(orthonormize(a))

print(time.time()-t)
