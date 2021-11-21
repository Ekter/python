from turtle import *

def setup(x,y,angle):
    setheading(angle)
    up()
    goto(x,y)
    down()
    tracer(0)

def troissept(taille,grosseur):

    t=taille
    tracer(0)
    setheading(0)

    width(grosseur)
    left(180)
    forward(t)
    backward(t)
    right(90)

    for i in range (2):
        forward(t)
        left(90)
        forward(t)
        backward(t)
        right(90)

    right(90)
    up()
    forward(t)
    down()

    forward(t)
    right(90)
    forward(2*t)

    update()

def Livrets(taille,x,y,angle=0,texte=0,couleur='red'):
    

    setup(x,y,angle)

    t=taille
    width(3*t)

    tracer(0)
    
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
    r,t1=pos()
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
    goto(r,t1)
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
    troissept(30*t,5*t)
    
    
    update()

Livrets(0.5,0,0)
input("")