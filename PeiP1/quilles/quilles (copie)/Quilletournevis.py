from setup import *

def tournevis (taille,x,y,angle=0):
    
    t=taille

    setup(x,y,angle)

    tracer(0)

    up()
    width(3*t)
    left(57)
    left(90)
    forward(t*9)
    right(90)
    down()

    fillcolor('#9bd9e5')
    for i in range(2):
        forward(t*16)
        right(90)
        forward(t*33)
        right(90)
    up()
    forward(t*16)
    right(90)
    forward(t*9)
    left(90)
    down()

    fillcolor('#c5d3da')
    begin_fill()
    forward(t*210)
    left(20)
    forward(t*10)
    right(25)
    forward(t*40)
    right(85)
    forward(t*15)
    right(85)
    forward(t*40)
    right(25)
    forward(t*10)
    left(20)
    forward(t*210)
    right(90)
    end_fill()

    up()
    forward(t*40)
    left(90)
    forward(t*50)
    down()
    fillcolor('#3686c8') 
    begin_fill()
    for i in range(2):
        forward(t*210)
        circle(t*32,180)
    end_fill()

    up()
    forward(t*10)
    left(90)
    forward(t*-12)
    right(90)
    down()

    fillcolor('#6ac188')
    begin_fill()
    for i in range(2):
        up()
        left(90)
        forward(t*25)
        right(90)
        down()


        for i in range(2):
            forward(t*190)
            circle(t*7,180)

    end_fill()
            

    up()
    forward(t*-20)
    left(90)
    forward(t*20)
    down()

    fillcolor('#9bd9e5')
    begin_fill()
    for i in range(2):
       left(90)
       forward(t*25)
       left(90)
       forward(t*50)
    end_fill()

    update()

