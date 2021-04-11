from turtle import *

def troissept(tortue,taille,grosseur):

    t=taille
    tracer(0)
    tortue.setheading(0)

    tortue.width(grosseur)
    tortue.left(180)
    tortue.forward(t)
    tortue.backward(t)
    tortue.right(90)

    for i in range (2):
        tortue.forward(t)
        tortue.left(90)
        tortue.forward(t)
        tortue.backward(t)
        tortue.right(90)

    tortue.right(90)
    tortue.up()
    tortue.forward(t)
    tortue.down()

    tortue.forward(t)
    tortue.right(90)
    tortue.forward(2*t)

    update()

