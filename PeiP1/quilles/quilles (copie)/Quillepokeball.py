from setup import *
def pokeball(taille,x,y,angle=0):
    
    setup(x,y,angle)
    
    t=taille


    tracer(0)

    width(3*t)
    up()
    forward(t*225)
    left(90)
    forward(t*8)
    right(90)
    down()
    left(268)

    fillcolor('white')
    begin_fill()
    circle(t*-218,360)
    end_fill()

    fillcolor('red')
    begin_fill()
    right(55)
    circle(t*-390,68)
    right(55)
    circle(t*-218,186.5)
    end_fill()

    fillcolor('black')
    begin_fill()
    right(45)
    circle(t*-270,31.5)
    left(80)
    circle(t*-70,175)
    left(85)
    circle(t*-270,36.5)
    right(44)
    circle(t*-218,10)
    right(132)
    circle(t*270,37.9)
    left(80)
    circle(t*-70,144)
    left(80)
    circle(t*270,35)
    right(130)
    circle(t*-218,10)
    end_fill()

    

    up()
    right(70)
    forward(t*180)
    down()
    right(80)
    fillcolor('white')
    begin_fill()
    circle(t*36,360)
    end_fill()
    

    update()
