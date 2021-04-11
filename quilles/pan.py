from setup import *

def pancarte(x,y,angle=0,elargir=1,agrlargeur=1):

    e=elargir
    a=agrlargeur

    tracer(0)

    up()
    backward(12)
    right(90)
    forward(160)
    left(90)
    down()

    fillcolor('#8f5218')
    begin_fill()

    for i in range(2):
        forward(25)
        left(90)
        forward(320*e)
        left(90)

    left(90)
    forward(320*e)
    left(120)
    forward(12)
    left(60)
    forward(308*e)
    left(50)
    forward(12)
    end_fill()

    up()
    backward(190)
    left(45)
    forward(10)
    right(5)
    down()

    begin_fill()
    for i in range(2):
        forward(300)
        left(90)
        forward(160*a)
        left(90)
    end_fill()
    
    update()


