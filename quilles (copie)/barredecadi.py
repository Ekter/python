from turtle import *
from trait import *
def barre(vrtc,hrzt,angle,taille,miroir=1,chuia=0):

    tracer(0)
    t=taille
    m=miroir
    
    up()
    j,k=pos()
    setheading(0)
    forward(t*vrtc)
    right(m*90)
    forward(t*hrzt)
    down()
    
    begin_fill()
    right(m*angle)
    forward(t*120)
    forward(chuia)
    right(m*70)
    
    up()
    forward(t*15)
    down()
    
    right(m*110)
    forward(t*10)
    trait(m,5,t,180)
    forward(t*40)
    
    up()
    forward(t*20)
    down()
    
    trait(m,5,t,180)
    forward(t*55)
    forward(chuia)
    end_fill()

    setheading(0)
    up()
    goto(j,k)
    down()

    update()
