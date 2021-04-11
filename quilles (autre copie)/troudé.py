from turtle import *
from ovale import *
def trou(tortue,angle,taille):

    tortue.setheading(angle)
    t=taille
    tracer(0)
    tortue.width(5*t)
    tortue.fillcolor('white')
    tortue.begin_fill()
    ovalerelatif(tortue,int(80*t),(2*t),(1*t))
    tortue.end_fill()
    tortue.pencolor('black')
    tortue.up()
    tortue.left(90)
    tortue.forward(7*t)
    tortue.right(90)
    tortue.down()
    tortue.width(1*t)
    tortue.fillcolor('black')
    tortue.begin_fill()
    ovalerelatif(tortue,int(35*t),(4*t),(3*t))
    tortue.end_fill()


    update()

