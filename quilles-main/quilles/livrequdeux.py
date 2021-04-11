from setup import *
from quatredeux import quatredeux

def Livreqd(taille,x,y,angle=0,texte=0,couleur='red'):

    setup(x,y,angle)

    t=taille

    tracer(0)
    width(3*t)
    
    up()
    backward(t*115)
    right(90)
    forward(t*152)
    left(98)
    down()


    #Couverture du livre
    fillcolor(couleur)
    begin_fill()
    for i in range(2):
        forward(t*185)
        left(82)
        forward(t*300)
        left(98)
    end_fill()
    
    #Dessous du livre
    setheading(0)
    left(90)
    begin_fill()
    forward(t*300)
    left(135)
    forward(t*17)
    left(45)
    forward(t*290)
    circle(t*20,90)
    forward(t*232)
    left(90)
    forward(t*300)
    left(90)
    forward(t*20)
    left(135)
    forward(t*10)
    right(45)
    forward(t*282)
    right(90)
    forward(t*210)
    left(90)
    forward(t*10)
    backward(t*10)
    right(90)
    circle(t*-20,60)
    end_fill()
    
    setheading(0)
    fillcolor('white')
    begin_fill()
    left(8)
    forward(t*185)
    left(82)
    forward(t*265)
    right(90)
    forward(t*25)
    r,t=pos()
    right(45)
    forward(t*27)
    right(45)
    forward(t*282)
    right(90)
    forward(t*210)
    circle(t*-20,60)
    end_fill()

    up()
    setheading(0)
    goto(r,t)
    down()
    
    right(90)
    forward(t*290)
    right(90)
    forward(t*190)

    up()
    right(90)
    forward(t*200)
    right(90)
    forward(t*50)
    down()
    quatredeux(30*t,5*t)
    
    
    update()

Livreqd(1,0,0)
