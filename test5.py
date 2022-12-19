#is 5+2=5 true? 
#what is the Plik constant?

import math
import sys


def add(a,b):
    if b==0:
        return a
    else:
        return 1+add(a,b-1)


def multiply(a,b):
    if b==1:
        return a
    else:
        return add(a,multiply(a,b-1))
    

def pow2(a,b):
    if b==1:
        return a
    else:
        return multiply(a,pow(a,b-1))

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())
# pow(10,10)
# print("a")

print(math.log(pow(3278,419),2))
