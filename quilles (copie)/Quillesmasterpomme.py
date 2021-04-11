from setup import *
def MasterPomme(taille,x,y,angle=0):

    setup(x,y,angle)
    
    t=taille
    
    tracer(0)
    
    #Pomme rouge
    
    width(8*t)
    pencolor('black')

    fillcolor('red')
    begin_fill()
    circle(150*t,180)
    backward(-50*t)
    circle(150*t,180)
    forward(50*t)
    end_fill()
    
    #Contour jaune
    width(8*t)
    pencolor(248/255,206/255,13/255)
    fillcolor(240/255,207/255,17/255)
    begin_fill()
    up()
    left(90)
    forward(75*t)
    down()
    
    right(180)
    circle(40*t,180)
    forward(120*t)
    circle(40*t,180)
    right(90)
    forward(50*t)  #trait horizontal
    right(90)
    circle(40*t,180)
    forward(120*t)
    circle(40*t,180)
    right(90)
    forward(50*t)  #trait horizontal
    end_fill()

    #Position du M
    
    up()
    forward(72*t)
    left(90)
    backward(20*t)
    down()
    
    i=1.2
    #Traçage du M en noir rempli de blanc
    
    pencolor('white')
    fillcolor('black')
    begin_fill()
    forward(130*i*t) #trait vers le haut
    left(90)
    forward(40*i*t) # trait horizontal
    left(40)
    forward(55*i*t) #trait cochi
    right(83)
    forward(55*i*t) #trait cochi
    left(42)
    forward(40*i*t) #trait horizontal
    left(90)
    forward(130*i*t) #trait vers le bas
    left(90)
    forward(40*i*t) #trait horizontal
    left(90)
    forward(75*i*t) #ti trait vertical
    right(135)
    forward(55*i*t) #trait cochi
    left(85)
    forward(55*i*t) #trait cochi
    right(129)
    forward(75*i*t) #ti trait vertical
    left(90)
    forward(40*i*t)  #trait horizontal
    end_fill()
    
    #Position tige
    up()
    backward(80*t)
    right(90)
    backward(300*t)
    right(90)
    down()
    
    #La tige verte
    right(90)
    width(3*t)
    pencolor('black')
    fillcolor('green')
    begin_fill()
    circle(15*t,180)
    forward(100*t)
    circle(15*t,180)
    forward(100*t)
    end_fill()

    #Position feuille
    up()
    backward(75*t)
    right(90)
    forward(10*t)
    down()

    #Feuille1
    right(30)
    fillcolor('green')
    begin_fill()
    circle(75*t,100)
    circle(20*t,60)
    circle(20*t,60)
    circle(112.5*t,57)
    end_fill()

    #Position feuille2
    up()
    right(70)
    forward(50*t)
    right(30)
    down()

    #Feuille2
    left(70)
    fillcolor('green')
    begin_fill()
    circle(-75*t,100)
    circle(-20*t,60)
    circle(-20*t,60)
    circle(-112.5*t,57)
    end_fill()
    penup()
    goto(600,600)
    update()





