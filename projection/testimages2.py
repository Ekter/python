from typing import Tuple
import cv2 as cv
import numpy as np
import random
import math

matrice = cv.imread("Lena.png")
print(matrice.shape)
print(matrice[0, 0])
matrice.tofile("Lena2.png")
matrice2 = matrice.copy()

def premier(n:int)-> bool:
    m=1
    if m%2==0:
        return False
    while m<math.sqrt(n):
        if n%m==0:
            return False
        m+=2
    return True

def degrade(lenght: int, weight: int, col1: Tuple[int, int, int] = (0, 0, 0), col2: Tuple[int, int, int] = (128, 128, 128)):
    matrice = [[(0, 0, 0) for _ in range(lenght)] for _ in range(lenght)]
    weight2 = 1
    for i in range(lenght):
        for j in range(weight):
            a, b, c = matrice[i][j]
            matrice[i][j] = ((j/weight)*col1[0]+(1-j/weight)*col2[0]+a, (j/weight) *
                             col1[1]+(1-j/weight)*col2[1]+b, (j/weight)*col1[2]+(1-j/weight)*col2[2]+c)
        print(i)
    return matrice

def degradev2(lenght: int, weight: int):
    matrice = [[(0, 0, 0) for _ in range(lenght)] for _ in range(lenght)]
    weight2 = 1
    for i in range(lenght):
        for j in range(weight):
            a, b, c = matrice[i][j]
            matrice[i][j] = int(premier(i+weight*j))
        print(i)
    return matrice



# cv.waitKey(0)
# cv.destroyAllWindows()
for i in range(0, 255, 25):
    cv.imwrite(f"test1degrade{i//25}.png", np.array(
        degrade(100, 100, (i, i, i), (i+25, i+25, i+25))))
cv.imwrite(f"test1degrade{i//25}.png", np.array(degradev2(100, 100)))