from turtle import *

def quatredeux(taille,grosseur,tortue):

    t=taille
    tracer(0)
    tortue.setheading(0)
    tortue.width(grosseur)
    tortue.left(90)
    tortue.forward(2*t)
    tortue.backward(t)
    tortue.left(90)
    tortue.forward(t)
    tortue.right(90)
    tortue.forward(t)
    tortue.right(90)
    tortue.up()
    tortue.forward(t*2)
    tortue.down()
    for i in range (2):
        tortue.forward(t)
        tortue.right(90)
    tortue.forward(t)
    tortue.left(90)
    tortue.forward(t)
    tortue.left(90)
    tortue.forward(t)
    

    update()



    
    
