from __future__ import annotations
from typing import List, Tuple
import cv2 as cv
import numpy as np


class MatrixImage():
    def __init__(self, mat: List[List[Tuple(int, int, int)]]) -> None:
        i = len(mat)
        j = len(mat[0])
        for l in mat:
            if len(l) != j:
                raise ValueError("Les lignes ne sont pas de la même longueur")
        self.mat = mat

    def __add__(self, other: MatrixImage) -> MatrixImage:
        return MatrixImage([[[a+b for a, b in (self.mat[i][j], other.mat[i][j])] for j in range(len(self.mat[i]))] for i in range(len(self.mat))])

    def __repr__(self) -> str:
        return str(self.mat)


def degradev2(lenght: int, weight: int) -> List[List[Tuple[int, int, int]]]:
    matrice = [[[0, 0, 0] for _ in range(weight)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            matrice[i][j] = [1, 2, 3]
    return matrice


print(MatrixImage(degradev2(10, 10))+MatrixImage(degradev2(10, 10)))
cv.imwrite(f"test2degrade.png", np.array(degradev2(100, 100)))
