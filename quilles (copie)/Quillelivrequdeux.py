from setup import *
from quatredeux import quatredeux

def Livreqd(taille,x,y,angle=0,texte=0,couleur='red'):

    setup(x,y,angle)

    t=taille

    tracer(0)
    width(3*t)
    
    up()
    backward(115)
    right(90)
    forward(152)
    left(98)
    down()


    #Couverture du livre
    fillcolor(couleur)
    begin_fill()
    for i in range(2):
        forward(185)
        left(82)
        forward(300)
        left(98)
    end_fill()
    
    #Dessous du livre
    setheading(0)
    left(90)
    begin_fill()
    forward(300)
    left(135)
    forward(17)
    left(45)
    forward(290)
    circle(20,90)
    forward(232)
    left(90)
    forward(300)
    left(90)
    forward(20)
    left(135)
    forward(10)
    right(45)
    forward(282)
    right(90)
    forward(210)
    left(90)
    forward(10)
    backward(10)
    right(90)
    circle(-20,60)
    end_fill()
    
    setheading(0)
    fillcolor('white')
    begin_fill()
    left(8)
    forward(185)
    left(82)
    forward(265)
    right(90)
    forward(25)
    r,c=pos()
    right(45)
    forward(27)
    right(45)
    forward(282)
    right(90)
    forward(210)
    circle(-20,60)
    end_fill()

    up()
    setheading(0)
    goto(r,c)
    down()
    
    right(90)
    forward(290)
    right(90)
    forward(190)

    up()
    right(90)
    forward(200)
    right(90)
    forward(50)
    down()
    quatredeux(30,5)
    
    
    update()
