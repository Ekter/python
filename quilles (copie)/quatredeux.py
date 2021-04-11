from turtle import *

def quatredeux(taille,grosseur):

    t=taille
    tracer(0)
    setheading(0)

    width(grosseur)

    left(90)
    forward(2*t)
    backward(t)
    left(90)
    forward(t)
    right(90)
    forward(t)
    right(90)
    up()
    forward(t*2)
    down()

    for i in range (2):
        forward(t)
        right(90)
    forward(t)
    left(90)
    forward(t)
    left(90)
    forward(t)
    

    update()



    
    
