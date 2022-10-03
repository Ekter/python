# from typing import Literal
import random
from typing import Callable, List

dic_result = {(False, False): False, (False, True): True,
              (True, False): True, (True, True): True}

functions = [lambda x, y:True, lambda x, y:False, lambda x, y:x, lambda x, y:y,
             lambda x, y:x or y, lambda x, y: not x, lambda x, y: not y, lambda x, y:x and y]
resal = [1]
ia=[[random.choice(functions) for _ in range(n)] for n in resal]

# ia = [[lambda x, y:x or y, lambda x, y:x and y], [
#     lambda x, y:x, lambda x, y:not y], [lambda x, y:x and y]]


def calculus(x, y, IA):
    for line in IA[:-1]:
        x, y = line[0](x, y), line[1](x, y)
    return IA[-1][0](x, y)


def test(x: bool, y: bool, IA):
    return dic_result[(x, y)] == calculus(x, y, ia)


def full_test(IA):
    l = []
    for x in [True, False]:
        for y in [True, False]:
            # print(x,y," -> ",calculus(x,y))
            b=test(x, y, IA)
            l.append(b)
            if b:
                print(x, y, " -> ", calculus(x, y, IA))
    return sum(l) == len(l)


def main():
    n = 1
    ia=[[random.choice(functions) for _ in range(n)] for n in resal]
    while not full_test(ia):
        # ia=[[random.choice(functions),random.choice(functions)], [random.choice(functions),random.choice(functions)], [random.choice(functions)]]
        ia=[[random.choice(functions) for _ in range(n)] for n in resal]
        print(ia)
        print(full_test(ia))
        print(n)
        n += 1


if __name__ == "__main__":
    main()
