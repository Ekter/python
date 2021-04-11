from setup import *
from pan import pancarte

def stock(taille,x,y,angle=0):

    screen=Screen()
    screen.bgpic('planche.gif')

    setup(x,y,angle)

    t=taille

    tracer(0)

    up()
    backward(245)
    right(90)
    forward(92)
    left(90)
    down()

    #Planche
    fillcolor('#d49335')
    begin_fill()
    forward(490)
    left(50)
    forward(16)
    left(50)
    for i in range(2):
        forward(40)
        right(20)
        forward(40)
        left(20)
    left(20)
    forward(16)
    left(60)
    forward(500)
    left(45)
    forward(10)
    left(53)
    circle(-800,10.5)
    right(50)
    forward(7)
    left(70)
    forward(30)
    #end_fill()

    #Contour relief
    fillcolor('#6e4320')
    begin_fill()
    right(150)
    forward(6)
    right(30)
    forward(30)
    right(70)
    forward(7)
    left(50)
    circle(800,10.3)
    right(53)
    forward(10)
    right(53)
    forward(6)
    right(128)
    forward(10)
    left(53)
    circle(-800,10.5)
    right(50)
    forward(7)
    left(70)
    forward(30)
    end_fill()

    up()
    left(74)
    forward(495)
    right(30)
    down()

    begin_fill()
    forward(6)
    left(80)
    forward(16)
    left(50)
    for i in range(2):
        forward(40)
        right(20)
        forward(40)
        left(20)
    forward(7)
    left(20)
    forward(14)
    w,d=pos()
    left(80)
    forward(4)
    left(95)
    forward(16)
    right(35)
    for i in range(2):
        forward(40)
        left(20)
        forward(40)
        right(20)
    right(30)
    forward(16)
    g,h=pos()
    end_fill()
    
    up()
    goto(w,d)
    right(50.2)
    down()

    begin_fill()
    forward(505)
    left(160)
    forward(6)
    left(20)
    forward(490)
    end_fill()

    up()
    goto(g,h)
    down()

    
    begin_fill()
    left(180)
    forward(500)
    left(160)
    forward(6)
    left(20)
    forward(490)
    end_fill()

    pencolor('#c1772c')
    width(3)
    up()
    left(90)
    forward(10)
    left(80)
    down()
    circle(1400,20)


    
        

 
    
    
    
    update()

stock(1,0,0)
