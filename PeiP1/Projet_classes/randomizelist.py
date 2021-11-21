#/usr/bin/python3
from random import randint
def randomize(l : list):
    l2=[]
    while len(l)>0:
        l2.append(l.pop(randint(0,len(l)-1)))
    return l2
for i in range(10):
    l3=randomize(["🍇","🍋","🥥","Le perdant","🍏","🍄","🍅","🍍","🍑","🥑","🥒","🥔"])
    print("Equipe 1:                     Equipe 2:\n","\n".join([str(l3[i])+" "*(30-len(str(l3[i])))+str(l3[i+int(len(l3)/2)]) for i in range(0,int(len(l3)/2))]),sep="")
input()