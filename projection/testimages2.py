from timeit import default_timer as timer
from time import time
from typing import Tuple
import cv2 as cv
import numpy as np
import random
import math
from numba import jit, cuda, vectorize
import matplotlib.pyplot as plt

# matrice = cv.imread("Lena.png")
# print(matrice.shape)
# print(matrice[0, 0])
# matrice.tofile("Lena2.png")
# matrice2 = matrice.copy()

# @vectorize(["boolean(int16)"], target='cpu')

@jit(nopython=True,nogil=True,parallel=True)
def premier(n:int)-> bool:
    m=2
    r = math.sqrt(n)
    while m <= r:
        if n % m == 0:
            return False
        m += 1
    return n > 1


def premier2(n: int) -> bool:
    m = 2
    r = math.sqrt(n)
    while m <= r:
        if n % m == 0:
            return False
        m += 1
    return n > 1


def degrade(lenght: int, weight: int, col1: Tuple[int, int, int] = (0, 0, 0), col2: Tuple[int, int, int] = (128, 128, 128)):
    matrice = [[(0, 0, 0) for _ in range(lenght)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            a, b, c = matrice[i][j]
            matrice[i][j] = ((j/weight)*col1[0]+(1-j/weight)*col2[0]+a, (j/weight) *
                             col1[1]+(1-j/weight)*col2[1]+b, (j/weight)*col1[2]+(1-j/weight)*col2[2]+c)
        print(i)
    return matrice


# @jit(nopython=True, nogil=True)
# @vectorize(["(int32, int32)"], target='cuda')
def degradev2(lenght: int, weight: int):
    matrice = [[(0, 0, 0) for _ in range(weight)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            p = premier((weight*i+j)*2+1)*255
            matrice[i][j] = p
        print(i)
    return matrice


def degradev3(lenght: int, weight: int):
    matrice = [[(0, 0, 0) for _ in range(weight)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            p = premier2(weight*i+j)*255
            matrice[i][j] = p
            
        print(i)
    return matrice

# cv.waitKey(0)
# cv.destroyAllWindows()
# for i in range(0, 255, 25):
#    cv.imwrite(f"test1degrade{i//25}.png", np.array(
#        degrade(100, 100, (i, i, i), (i+25, i+25, i+25))))

t=time()
# l=degradev2(100,100)
cv.imwrite(f"test2degrade.png", np.array(degradev2(10000,10000)))
plt.imshow(degradev2(1000,1000))
plt.show()
a=time()-t

t=time()
# l=degradev3(100,100)
cv.imwrite(f"test3degrade.png", np.array(degradev3(100,100)))
print(a)
print(time()-t)


# # to measure exec time

# # This should be a substantially high value. On my test machine, this took
# # 33 seconds to run via the CPU and just over 3 seconds on the GPU.
# NUM_ELEMENTS = 10000000

# # This is the CPU version.

# @vectorize(["float32(float32, float32)"], target='cpu')
# def vector_add_cpu(a, b):
#     c = np.zeros(NUM_ELEMENTS, dtype=np.float32)
#     for i in range(NUM_ELEMENTS):
#         c[i] = a[i] + b[i]
#     return c
a   
# # This is the GPU version. Note the @vectorize decorator. This tells
# # numba to turn this into a GPU vectorized function.


# @vectorize(["float32(float32, float32)"], target='cuda')
# def vector_add_gpu(a, b):
#     return a + b


# def main():
#     a_source = np.ones(NUM_ELEMENTS, dtype=np.float32)
#     b_source = np.ones(NUM_ELEMENTS, dtype=np.float32)

#     # Time the CPU function
#     start = time()
#     vector_add_cpu(a_source, b_source)
#     vector_add_cpu_time = time() - start

#     # Time the GPU function
#     start = time()
#     vector_add_gpu(a_source, b_source)
#     vector_add_gpu_time = time() - start

#     # Report times
#     print("CPU function took %f seconds." % vector_add_cpu_time)
#     print("GPU function took %f seconds." % vector_add_gpu_time)

#     return 0


# if __name__ == "__main__":
#     main()
