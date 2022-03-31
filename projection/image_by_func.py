from calendar import c
from time import sleep, time
import cv2 as cv
import numpy as np
import math
from numba import jit
from random import randint as ri

@jit(nopython=True,nogil=True,parallel=True)
def premier(n:int)-> bool:
    m=2
    r = math.sqrt(n)
    while m <= r:
        if n % m == 0:
            return False
        m += 1
    return n > 1


@jit(nopython=True, nogil=True)
def degradev2(lenght: int, weight: int):
    matrice = [[(0, 0, 0) for _ in range(weight)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            p = premier((weight*i+j)*2+1)*255
            matrice[i][j] = p
        print(i)
    return matrice

# @jit(nopython=True, nogil=True)
def degrade(lenght: int, weight: int,func=lambda x:premier(2*x+1)*255):
    matrice = [[(0, 0, 0) for _ in range(weight)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            p = func(lenght*i+j)
            matrice[i][j] = p
        print(i)
    return matrice

# n=1000
# t=time()
# # l=degradev2(100,100)
# cv.imwrite(f"degradefunc.png", np.array(degrade(n,n,func=lambda x:x%5*37+x%37)))
# print(time()-t)

if __name__=="__main__":
    while True:
        a=ri(2,10)
        b=ri(2,50)
        c=ri(2,10)
        d=ri(2,50)
        cv.imwrite("degradefunc.png",np.array(degrade(720,1080,func=lambda x:x%a*b+x%c*d)))
        sleep(10)
