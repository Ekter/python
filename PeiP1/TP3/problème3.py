#/usr/bin/python3
from turtle import *
from math import acos,pi,cos,sqrt
up()
goto((-300,-200))
down()

nbPoly=int(input("Nombre de polygones?"))
nbCote=int(input("Nombre de côtés?"))
l=int(input("Longueur?"))
f=float(input("Facteur(0-1)?"))
angleCote=360/nbCote
speed(0)
a=(1-f)*l
b=f*l
c=sqrt(a**2+b**2-2*a*b*cos(2*pi*angleCote/360))
alpha=acos((a**2+c**2-b**2)/(2*a*c))
for n in range(nbPoly):
    for k in range(nbCote):
        forward(l)
        left(angleCote)
    a=(1-f)*l
    b=f*l
    c=sqrt(a**2+b**2-2*a*b*cos(2*pi*angleCote/360))
    #alpha=acos((a**2+c**2-b**2)/(2*a*c))
    forward(b)
    print(alpha/2/pi*360,c)
    left(alpha/2/pi*360)
    l=c

input()
