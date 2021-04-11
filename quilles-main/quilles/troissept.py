from turtle import *

def troissept(taille,grosseur):

    t=taille
    tracer(0)
    setheading(0)

    width(grosseur)
    left(180)
    forward(t)
    backward(t)
    right(90)

    for i in range (2):
        forward(t)
        left(90)
        forward(t)
        backward(t)
        right(90)

    right(90)
    up()
    forward(t)
    down()

    forward(t)
    right(90)
    forward(2*t)

    update()

