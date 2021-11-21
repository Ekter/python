from setup import *
def masque(taille,x,y,angle=0):

    setup(x,y,angle)
    
    t=taille

    tracer(0)

    width(t*2*t)
    pencolor('black')
    fillcolor('#c5e2f3')
    
    up()
    backward(t*145)
    left(90)
    forward(t*90)
    right(110)
    down()

    #Couvrebouche    
    begin_fill()
    circle(t*440,37.5)
    right(105)
    forward(t*150)
    right(65)
    circle(t*-310,55.6)
    right(61)
    forward(t*151)
    end_fill()

    up()
    backward(t*40)
    right(90)
    forward(t*30)
    right(25)
    u,i=pos()
    down()

    #Pli de masque
    for i in range (20):
        width(t*2+0.1*i)
        circle(t*350,1)

    left(6)

    for i in range(20):
        width(t*4-0.1*i)
        circle(t*350,1)

    up()
    goto(u,i)
    right(120)
    forward(t*15)
    left(75)
    down()
    

    for i in range (20):
        width(t*2+0.1*i)
        circle(t*350,1)

    left(6)

    for i in range(20):
        width(t*4-0.1*i)
        circle(t*350,1)

    up()
    goto(u,i)
    right(120)
    forward(t*55)
    left(73)
    down()

    for i in range (20):
        width(t*2+0.1*i)
        circle(t*350,1)

    left(6)

    for i in range(20):
        width(t*4-0.1*i)
        circle(t*350,1)

    up()
    forward(t*20)
    right(70)
    forward(t*15)
    left(73)
    down()

    #Les deux languettes

    fillcolor('#cbc4ba')
    begin_fill()
    circle(t*300,14)
    circle(t*57,116)
    left(50)
    forward(t*60)
    right(110)
    forward(t*15)
    right(70)
    forward(t*50)
    right(25)
    circle(t*-60,130)
    left(6)
    circle(t*-134,30)
    forward(t*35)
    right(110)
    forward(t*15)
    end_fill()
    
    up()
    left(84)
    forward(t*288)
    left(90)
    forward(t*16)
    right(90)
    down()

    begin_fill()
    right(23)
    circle(t*-300,17)
    left(5)
    circle(t*-63,138)
    right(30)
    forward(t*50)
    right(74)
    forward(t*14)
    right(110)
    forward(t*50)
    left(50)
    circle(t*60,130)
    right(6)
    circle(t*134,10)
    left(5)
    forward(t*32)
    right(82)
    forward(t*20)
    end_fill()

    update()
