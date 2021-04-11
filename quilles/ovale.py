from turtle import*
from math import*

def ovalerelatif(tortue,prec,longueur,ecrasement,scale=1):
    for i in range(prec):
        tortue.forward((longueur + ecrasement*cos(i/prec*2*pi*2))/scale)
        tortue.left(360/prec)
