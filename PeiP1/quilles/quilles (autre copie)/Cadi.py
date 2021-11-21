from trait import *
from ovale import *
from barredecadi import *
from setup import setup

def cadi(taille,x,y,angle,miroir=1):

    m=miroir
    t=taille

    tortuecadi=Turtle(undobuffersize=0)#,visible=False)#,shape="square")
    setup(x,y,angle,tortuecadi)

    tracer(0)

    tortuecadi.up()
    tortuecadi.forward(70)
    tortuecadi.right(m*90)
    tortuecadi.forward(70)
    tortuecadi.left(m*90)
    tortuecadi.down()

    #Le cadre du cadi
    tortuecadi.pencolor('black')
    tortuecadi.fillcolor('#E9DCA8')
    tortuecadi.begin_fill()
    
    tortuecadi.width(1*t)
    tortuecadi.right(m*40)
    tortuecadi.circle(m*-100*t,43)
    tortuecadi.circle(m*-5*t,100)
    tortuecadi.circle(m*2000*t,5)
    tortuecadi.right(m*3)
    tortuecadi.circle(m*2000*t,3.65)
    tortuecadi.circle(m*9*t,180)
    trait(tortuecadi,m,20,1*t,0,0)
    tortuecadi.forward(100*t)
    tortuecadi.right(m*3)
    tortuecadi.forward(180*t)
    tortuecadi.right(m*3)
    trait(tortuecadi,m,5,1*t,0,10)
    tortuecadi.forward(40*t)
    tortuecadi.circle(m*7*t,95)
    for j in range (14):
        tortuecadi.circle(m*130*t,3) 
        trait(tortuecadi,m,1,1*t)
    tortuecadi.right(m*60)
    for j in range (27):
        trait(tortuecadi,m,1,1*t)
        tortuecadi.circle(m*(-800)*t,0.5)

    tortuecadi.circle(m*t*-10,59)
    trait(tortuecadi,m,7,t,0,15)
    tortuecadi.circle(m*t*(-700),3)
    tortuecadi.right(m*2)
    trait(tortuecadi,m,2,t)
    tortuecadi.circle(m*t*100,10)
    tortuecadi.circle(m*t*30,28)
    tortuecadi.circle(m*t*12,160)
    tortuecadi.right(m*10)
    
    w,x=tortuecadi.pos()
    tortuecadi.up()
    tortuecadi.forward(t*5)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*5)
    tortuecadi.right(m*90)
    tortuecadi.down()
    
    tortuecadi.up()
    tortuecadi.goto(w,x)
    tortuecadi.down()
    
    tortuecadi.forward(t*55)
    tortuecadi.circle(m*t*30,60)
    tortuecadi.forward(t*45)
    c,v=tortuecadi.pos()
    
    tortuecadi.circle(m*t*1000,9)
    tortuecadi.right(m*9)
    tortuecadi.end_fill()

    tortuecadi.up()
    tortuecadi.goto(c,v)
    tortuecadi.down()

    #La cage du cadi
    tortuecadi.begin_fill()
    tortuecadi.circle(m*t*-10,65)
    tortuecadi.forward(t*150)
    tortuecadi.left(m*4.25)
    tortuecadi.forward(t*200)
    tortuecadi.circle(m*t*40,20)
    tortuecadi.circle(m*t*10,93)
    tortuecadi.forward(t*120)
    tortuecadi.left(m*2)
    tortuecadi.circle(m*t*48,35)
    tortuecadi.circle(m*t*10,30)
    trait(tortuecadi,m,38,t)
    tortuecadi.forward(t*240)

    tortuecadi.up()
    tortuecadi.forward(t*1)
    tortuecadi.left(m*67)
    tortuecadi.forward(t*20)
    tortuecadi.down()

    tortuecadi.left(m*113)
    tortuecadi.forward(t*250)
    tortuecadi.circle(m*t*-5,67)
    for j in range(10):
        trait(tortuecadi,m,1,t)
        tortuecadi.forward(t*5)
  
    tortuecadi.forward(t*20)
    for j in range(10):
        trait(tortuecadi,m,1,t)
        tortuecadi.forward(t*5)

    tortuecadi.circle(m*t*-5,115)

    for j in range(5):
        for j in range(8):
            trait(tortuecadi,m,1,t,0,15)
            tortuecadi.forward(t*5)
        tortuecadi.forward(t*20)
    
    for j in range(10):
        trait(tortuecadi,m,1,t,0,15)
        tortuecadi.forward(t*5)

    tortuecadi.end_fill()

    tortuecadi.up()
    tortuecadi.right(m*120)
    tortuecadi.forward(t*60)
    tortuecadi.right(m*60)
    tortuecadi.backward(t*5)
    tortuecadi.down()

    #Le trait du milieu
    tortuecadi.begin_fill()
    tortuecadi.forward(t*310)
    tortuecadi.left(m*120)
    tortuecadi.up()
    tortuecadi.forward(t*20)
    tortuecadi.down()
    tortuecadi.left(m*60)
    tortuecadi.forward(t*10)
    for j in range(5):
        for j in range(6):
            trait(tortuecadi,m,1,t)
            tortuecadi.forward(t*5)
        tortuecadi.forward(t*20)
    
    for j in range(6):
        trait(tortuecadi,m,1,t)
        tortuecadi.forward(t*5)
    tortuecadi.forward(t*5)
    tortuecadi.end_fill()
    


    #Barre verticales
    barre(tortuecadi,-40,75,172,t,m)
    
    barre(tortuecadi,-100,72,181,t,m)

    barre(tortuecadi,-162,69,189,t,m,5-5*m)

    barre(tortuecadi,-220,65,195,t,m,5-5*m)

    barre(tortuecadi,-280,62,200,t,m,5-5*m)
    
    
    #Roue arrière
    tortuecadi.fillcolor('#302F2B')
    tortuecadi.up()
    tortuecadi.backward(10*t)
    tortuecadi.right(90*m)
    tortuecadi.forward(160*t*m)
    tortuecadi.left(95*m)
    tortuecadi.right(90+90*-m)
    
    tortuecadi.down()
    tortuecadi.begin_fill()
    tortuecadi.circle(m*t*-23,300)
    tortuecadi.end_fill()
    
    tortuecadi.up()
    tortuecadi.forward(t*14)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*-19)
    tortuecadi.right(m*170)
    tortuecadi.down()

    tortuecadi.fillcolor('#B2B2B2')
    tortuecadi.begin_fill()
    tortuecadi.circle(m*t*-14,275)
    tortuecadi.end_fill()

    tortuecadi.up()
    tortuecadi.forward(t*29)
    tortuecadi.left(m*105)
    tortuecadi.forward(t*17)
    tortuecadi.down()
    tortuecadi.left(m*22)
    tortuecadi.fillcolor('#787566')
    tortuecadi.begin_fill()
    tortuecadi.left(m*30)
    tortuecadi.circle(m*t*7,40)
    tortuecadi.forward(t*20)
    tortuecadi.left(m*47)
    tortuecadi.circle(m*t*50,35)
    tortuecadi.circle(m*t*5,160)
    tortuecadi.right(m*25)
    tortuecadi.circle(m*t*-50,35)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*20)
    tortuecadi.end_fill()

    tortuecadi.up()
    tortuecadi.backward(t*15)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*26)
    tortuecadi.down()

    tortuecadi.fillcolor('#5B5335')
    tortuecadi.begin_fill()
    tortuecadi.circle(m*t*4,360)
    tortuecadi.end_fill()

    
    tortuecadi.up()
    tortuecadi.setheading(0)
    tortuecadi.backward(m*t*250)
    tortuecadi.left(90*m)
    tortuecadi.forward(13*m*t)
    tortuecadi.right(85*m)
    tortuecadi.down()

    #Roue avant
    tortuecadi.fillcolor('#302F2B')
    tortuecadi.begin_fill()
    tortuecadi.right(90+90*-m)
    tortuecadi.up()
    tortuecadi.down()
    tortuecadi.circle(m*t*-23,300)
    tortuecadi.end_fill()
    
    tortuecadi.up()
    tortuecadi.forward(t*14)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*-19)
    tortuecadi.right(m*170)
    tortuecadi.down()

    tortuecadi.fillcolor('#B2B2B2')
    tortuecadi.begin_fill()
    tortuecadi.circle(m*t*-14,275)
    tortuecadi.end_fill()

    tortuecadi.up()
    tortuecadi.forward(t*29)
    tortuecadi.left(m*105)
    tortuecadi.forward(t*17)
    tortuecadi.down()
    tortuecadi.left(m*22)
    tortuecadi.fillcolor('#787566')
    tortuecadi.begin_fill()
    tortuecadi.left(m*30)
    tortuecadi.circle(m*t*7,40)
    tortuecadi.forward(t*20)
    tortuecadi.left(m*47)
    tortuecadi.circle(m*t*50,35)
    tortuecadi.circle(m*t*5,160)
    tortuecadi.right(m*25)
    tortuecadi.circle(m*t*-50,35)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*20)
    tortuecadi.end_fill()

    tortuecadi.up()
    tortuecadi.backward(t*15)
    tortuecadi.left(m*90)
    tortuecadi.forward(t*26)
    tortuecadi.down()

    tortuecadi.fillcolor('#5B5335')
    tortuecadi.begin_fill()
    tortuecadi.circle(m*t*4,360)
    tortuecadi.end_fill()
    
    update()
