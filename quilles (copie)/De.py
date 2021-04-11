from turtle import *
from dessinblocs import ovalerelatif
def undé(taille,x,y):
    """setup(900,700)
    screen=Screen()
    
    screen.bgpic('jeuxx.gif')"""

    #bgcolor('yellow')

    up()
    goto(x,y)
    down()

    t=taille

    tracer(0)

    up()
    forward(t*75)
    right(90)
    forward(t*130)
    left(90)
    down()

    width(1*t)
    pencolor('black')
    fillcolor('black')
    begin_fill()
    right(6)
    circle(t*1400,11.5)
    circle(t*5,100)
    left(10)
    circle(t*115,22)
    left(124)
    circle(t*-20,90)
    left(8.5)
    forward(t*239)
    left(90)
    forward(t*25)
    end_fill()

    begin_fill()
    circle(t*-20,65)
    right(2.5)
    forward(t*200)
    circle(t*-55,58)
    left(11)
    forward(t*175)
    left(60)
    circle(t*7,100)
    left(10.5)
    forward(t*160)
    circle(t*90,72)
    right(17)
    forward(t*206)
    circle(t*20,100)
    forward(t*15)
    left(70)
    forward(t*27)
    end_fill()

    fillcolor('white')
    begin_fill()
    width(4*t)
    right(101)
    forward(t*240)
    circle(t*40,80)
    right(15)
    for i in range(154):
        width(3.2+0.02*i)
        forward(t*1)
    
    circle(t*45,55)
    right(11)
    forward(t*210)
    circle(t*20,74)
    for i in range(239):
        width(6.08-0.01*i)
        forward(t*1)
    width(3)
    circle(t*50,60)
    forward(t*40)
    (k,l)=pos()
    forward(t*110)
    circle(t*60,50)
    forward(t*205)
    circle(t*26,60)
    end_fill()

    right(110)
    up()
    goto(k,l)
    backward(5)
    left(90)
    forward(t*255)
    right(46)
    down()
    angle=[0,141,116]
    trait=[229,168,255]
    for i in range (3):
        left(angle[i])
        (a,b)=pos()
        for j in range(trait[i]):
            width(10-0.03*j)
            forward(t*1)
        goto(a,b)
        
    up()
    backward(84)
    left(90)
    forward(t*210)
    down()
    begin_fill()
    width(5)
    left(75)
    pencolor('black')
    forward(t*105)
    circle(t*-20,78)
    forward(t*250)
    width(8)
    circle(t*-18,83)
    forward(t*120)
    (r,t)=pos()
    circle(t*-100,14)
    for i in range (210):
        width(8-0.035*i)
        forward(t*1)
    
    circle(t*-20,85)
    forward(t*246)
    right(89)
    forward(t*223)
    left(15)
    circle(t*43,70)
    end_fill()   
    up()
    left(100)
    goto(r,t)
    
    down()
    width(6)
    circle(t*-10,95)
    for i in range (260):
        width(6-0.015*i)
        forward(t*1)
    ht()
    end_fill()
        
    update()

undé(1,0,0)
    
