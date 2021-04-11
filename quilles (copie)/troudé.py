from turtle import *
from ovale import *
def trou(angle,taille):

    setheading(angle)
    t=taille

    tracer(0)

    width(5*t)
    fillcolor('white')
    begin_fill()
    ovalerelatif(int(80*t),(2*t),(1*t))
    end_fill()
    
    pencolor('black')
    up()
    left(90)
    forward(7*t)
    right(90)
    down()
    width(1*t)
    fillcolor('black')
    begin_fill()
    ovalerelatif(int(35*t),(4*t),(3*t))
    end_fill()


    update()

