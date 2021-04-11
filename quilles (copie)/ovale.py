from turtle import*
from math import*

def ovalerelatif(prec,longueur,ecrasement,scale=1):
    for i in range(prec):
        forward((longueur + ecrasement*cos(i/prec*2*pi*2))/scale)
        left(360/prec)
