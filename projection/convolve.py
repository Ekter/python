import numpy as np
from typing import Any

def convolve_3d(filter:np.ndarray, array:np.ndarray) -> np.ndarray:
    #filter is 2d, array is 3d
    #filter is 3x3
    final: np.ndarray[Any, np.dtype[np.floating]] = np.zeros(array.shape)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            for k in range(filter.shape[0]):
                for l in range(filter.shape[1]):
                    final[i][j] += array[i][j] * filter[k][l]
    return final
