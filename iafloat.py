import random
import math
import numpy as np
from typing import Callable, Iterable


class Model:
    """Little IA model"""

    act_functions: list[Callable[[Iterable[float]], float]] = [
        lambda x: max(0, np.sum(x)),
        lambda x: np.sum(x),
        lambda _: 1,
        lambda x: 1 / (1 + math.exp(-np.sum(x))),
        lambda x: 2 / (1 + math.exp(-2 * np.sum(x))) - 1,
    ]
    "Activation functions"

    def __init__(self, size: np.ndarray[int]) -> None:
        self.size = size
        self.weights: list[list[list[int]]] = np.ones((len(size)-1, max(size), max(size)))
        self.functions = [[self.rand_func() for _ in range(n)] for n in size]

    def rand_func(self) -> Callable[[Iterable[float]], float]:
        return random.choice(Model.act_functions)

    def compute(self, input_: np.ndarray[int]) -> None:
        assert len(input_) == self.size[0]

        curr: np.ndarray(np.float64) = input_
        for i in np.nditer(self.size[1:]):
            next_ = np.zeros(self.size[i])
            curr = curr * self.weights[i][0, 0:len(curr)-1].T
            for j in range(i):
                next_[j] = self.functions[i][j](curr)
            curr = next_[:]

m = Model(np.array([2, 3, 2]))
m.compute(np.array([1, -10]))






def main():
    return
    n = 1
    ia = [[random.choice(functions) for _ in range(n)] for n in resal]
    while not full_test(ia):
        # ia=[[random.choice(functions),random.choice(functions)], [random.choice(functions),random.choice(functions)], [random.choice(functions)]]
        ia = [[random.choice(functions) for _ in range(n)] for n in resal]
        print(ia)
        print(full_test(ia))
        print(n)
        n += 1
    for x, y in dic_result.keys():
        print(x, y, " -> ", calculus(x, y, ia))


if __name__ == "__main__":
    main()
