from trait import *
from ovale import *
from barredecadi import *
from setup import setup

def cadi(taille,x,y,angle,miroir=1):

    m=miroir
    t=taille

    setup(x,y,angle)

    tracer(0)

    up()
    forward(70)
    right(m*90)
    forward(70)
    left(m*90)
    down()

    #Le cadre du cadi
    pencolor('black')
    fillcolor('#E9DCA8')
    begin_fill()
    
    width(1*t)
    right(m*40)
    circle(m*-100*t,43)
    circle(m*-5*t,100)
    circle(m*2000*t,5)
    right(m*3)
    circle(m*2000*t,3.65)
    circle(m*9*t,180)
    trait(m,20,1*t,0,0)
    forward(100*t)
    right(m*3)
    forward(180*t)
    right(m*3)
    trait(m,5,1*t,0,10)
    forward(40*t)
    circle(m*7*t,95)
    for j in range (14):
        circle(m*130*t,3) 
        trait(m,1,1*t)
    right(m*60)
    for j in range (27):
        trait(m,1,1*t)
        circle(m*(-800)*t,0.5)

    circle(m*t*-10,59)
    trait(m,7,t,0,15)
    circle(m*t*(-700),3)
    right(m*2)
    trait(m,2,t)
    circle(m*t*100,10)
    circle(m*t*30,28)
    circle(m*t*12,160)
    right(m*10)
    
    w,x=pos()
    up()
    forward(t*5)
    left(m*90)
    forward(t*5)
    right(m*90)
    down()

    ovalerelatif(int(30*t),2*t,1*t)
    
    up()
    goto(w,x)
    down()
    
    forward(t*55)
    circle(m*t*30,60)
    forward(t*45)
    c,v=pos()
    
    circle(m*t*1000,9)
    right(m*9)
    end_fill()

    up()
    goto(c,v)
    down()

    #La cage du cadi
    begin_fill()
    circle(m*t*-10,65)
    forward(t*150)
    left(m*4.25)
    forward(t*200)
    circle(m*t*40,20)
    circle(m*t*10,93)
    forward(t*120)
    left(m*2)
    circle(m*t*48,35)
    circle(m*t*10,30)
    trait(m,38,t)
    forward(t*240)

    up()
    forward(t*1)
    left(m*67)
    forward(t*20)
    down()

    left(m*113)
    forward(t*250)
    circle(m*t*-5,67)
    for j in range(10):
        trait(m,1,t)
        forward(t*5)
  
    forward(t*20)
    for j in range(10):
        trait(m,1,t)
        forward(t*5)

    circle(m*t*-5,115)

    for j in range(5):
        for j in range(8):
            trait(m,1,t,0,15)
            forward(t*5)
        forward(t*20)
    
    for j in range(10):
        trait(m,1,t,0,15)
        forward(t*5)

    end_fill()

    up()
    right(m*120)
    forward(t*60)
    right(m*60)
    backward(t*5)
    down()

    #Le trait du milieu
    begin_fill()
    forward(t*310)
    left(m*120)
    up()
    forward(t*20)
    down()
    left(m*60)
    forward(t*10)
    for j in range(5):
        for j in range(6):
            trait(m,1,t)
            forward(t*5)
        forward(t*20)
    
    for j in range(6):
        trait(m,1,t)
        forward(t*5)
    forward(t*5)
    end_fill()

    #Barre verticales
    barre(-40,75,172,t,-m)
    
    barre(-100,72,181,t,-m)

    barre(-162,69,189,t,-m)

    barre(-220,65,195,t,-m)

    barre(-280,62,200,t,-m,10)
    
    
    #Roue arrière
    fillcolor('#302F2B')
    up()
    backward(10*t)
    right(90*m)
    forward(160*t)
    left(95*m)
    
    down()
    begin_fill()
    circle(m*t*-23,300)
    end_fill()
    
    up()
    forward(t*14)
    left(m*90)
    forward(t*-19)
    right(m*170)
    down()

    fillcolor('#B2B2B2')
    begin_fill()
    circle(m*t*-14,275)
    end_fill()

    up()
    forward(t*29)
    left(m*105)
    forward(t*17)
    down()
    left(m*22)
    fillcolor('#787566')
    begin_fill()
    left(m*30)
    circle(m*t*7,40)
    forward(t*20)
    left(m*47)
    circle(m*t*50,35)
    circle(m*t*5,160)
    right(m*25)
    circle(m*t*-50,35)
    left(m*90)
    forward(t*20)
    end_fill()

    up()
    backward(t*15)
    left(m*90)
    forward(t*26)
    down()

    fillcolor('#5B5335')
    begin_fill()
    circle(m*t*4,360)
    end_fill()

    
    up()
    setheading(0)
    backward(t*250)
    left(90*m)
    forward(13*t)
    right(85*m)
    down()

    #Roue avant
    fillcolor('#302F2B')
    begin_fill()
    circle(m*t*-23,300)
    end_fill()
    
    up()
    forward(t*14)
    left(m*90)
    forward(t*-19)
    right(m*170)
    down()

    fillcolor('#B2B2B2')
    begin_fill()
    circle(m*t*-14,275)
    end_fill()

    up()
    forward(t*29)
    left(m*105)
    forward(t*17)
    down()
    left(m*22)
    fillcolor('#787566')
    begin_fill()
    left(m*30)
    circle(m*t*7,40)
    forward(t*20)
    left(m*47)
    circle(m*t*50,35)
    circle(m*t*5,160)
    right(m*25)
    circle(m*t*-50,35)
    left(m*90)
    forward(t*20)
    end_fill()

    up()
    backward(t*15)
    left(m*90)
    forward(t*26)
    down()

    fillcolor('#5B5335')
    begin_fill()
    circle(m*t*4,360)
    end_fill()
    
    update()

cadi(1,0,0,0,1)



