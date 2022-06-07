"""module to approximate a distribution by a function"""
from time import time
import math
from typing import List

list_functions=[lambda x : x,math.sin,math.sqrt,math.exp,math.log,lambda x : 12435230]

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



def dephase(list_inputs:List[float],list_outputs:List[float],funct,min_x=-100,max_x=100,complexity=5,value=0):
    if max_x-min_x<1/complexity:
        return funct,value
    dic_prec={}
    for x in linspace(min_x,max_x,complexity*20):
        s=0
        functest=lambda k : funct(k+x)
        for j in range(len(list_outputs)):
            s+=abs(list_outputs[j]-functest(list_inputs[j]))
        print(s)
        if dic_prec.get(s) is None:
            dic_prec[s]=[functest]
        else:
            dic_prec[s].append(functest)    # à demander à appoorva et rom2
    print(dic_prec)
    list_prec=list(dic_prec.keys())
    list_prec.sort()

    best_funct=funct
    max_prec=4351245
    for i in range(min(complexity,10)):
        n=0
        for j in dic_prec[list_prec[i]]:
            if n>complexity:
                break
            print(n)
            funct,prec=dephase(list_inputs,list_outputs,j,(max_x-min_x)/(complexity*20),-(max_x-min_x)/(complexity*20),complexity,list_prec[i])
            n+=1
            if max_prec>prec:
                max_prec=s
                best_funct=j
    return best_funct,max_prec



def linspace(min_f,max_f,nb):
    for i in range(nb+1):
        yield min_f+(max_f-min_f)*i/nb


if __name__=="__main__":
    f=lambda x: x-37
    s=type_func([i for i in range(1,100)],[f(i) for i in range(1,100)])
    print(s[0](5),s[1])
    s=type_func([i for i in range(1,100)],[f(i+1) for i in range(1,100)])
    print(s[0](5),s[1])
    s=type_func([i for i in range(101,200)],[f(i) for i in range(101,200)])
    print(s[0](5),s[1])
    s=type_func([i for i in range(101,200)],[f(i+1) for i in range(101,200)])
    print(s[0](5),s[1])
    t=time()
    funct,val=type_func([i for i in range(37,50)],[f(i) for i in range(0,50-37)])
    funct2,val=dephase([i for i in range(37,50)],[f(i) for i in range(0,50-37)],funct,-100,100,1,val)
    for x in range(10):
        print(funct2(x))
    print(time()-t)




