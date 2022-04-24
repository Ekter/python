"""module to approximate a distribution by a function"""
import math
from typing import List

list_functions=[lambda x : x,math.sin,math.sqrt,math.exp,math.log]

def type_func(list_inputs:List[float],list_outputs:List[float]):
    max_prec=4351245
    best_funct=lambda x : 0
    for i in list_functions:
        s=0
        for j in range(len(list_outputs)):
            s+=abs(list_outputs[j]-i(list_inputs[j]))
        if max_prec>s:
            max_prec=s
            best_funct=i
    return best_funct,max_prec












if __name__=="__main__":
    f=lambda x:math.log(x+1)
    s=type_func([i for i in range(1,100)],[f(i) for i in range(1,100)])
    print(s[0](5),s[1])
    s=type_func([i for i in range(1,100)],[f(i+1) for i in range(1,100)])
    print(s[0](5),s[1])
    s=type_func([i for i in range(101,200)],[f(i) for i in range(101,200)])
    print(s[0](5),s[1])
    s=type_func([i for i in range(101,200)],[f(i+1) for i in range(101,200)])
    print(s[0](5),s[1])
