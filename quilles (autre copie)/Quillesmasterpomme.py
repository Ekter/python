from setup import *
def masterpomme(taille,x,y,angle=0):
    y-=20*taille
    tortuemasterpomme=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuemasterpomme)
    
    t=taille/8
    
    tracer(0)
    
    #Pomme rouge
    
    tortuemasterpomme.width(8*t)
    tortuemasterpomme.pencolor('black')

    tortuemasterpomme.fillcolor('red')
    tortuemasterpomme.begin_fill()
    tortuemasterpomme.circle(150*t,180)
    tortuemasterpomme.backward(-50*t)
    tortuemasterpomme.circle(150*t,180)
    tortuemasterpomme.forward(50*t)
    tortuemasterpomme.end_fill()
    
    #Contour jaune
    tortuemasterpomme.width(8*t)
    tortuemasterpomme.pencolor(248/255,206/255,13/255)
    tortuemasterpomme.fillcolor(240/255,207/255,17/255)
    tortuemasterpomme.begin_fill()
    tortuemasterpomme.up()
    tortuemasterpomme.left(90)
    tortuemasterpomme.forward(75*t)
    tortuemasterpomme.down()
    
    tortuemasterpomme.right(180)
    tortuemasterpomme.circle(40*t,180)
    tortuemasterpomme.forward(120*t)
    tortuemasterpomme.circle(40*t,180)
    tortuemasterpomme.right(90)
    tortuemasterpomme.forward(50*t)  #trait horizontal
    tortuemasterpomme.right(90)
    tortuemasterpomme.circle(40*t,180)
    tortuemasterpomme.forward(120*t)
    tortuemasterpomme.circle(40*t,180)
    tortuemasterpomme.right(90)
    tortuemasterpomme.forward(50*t)  #trait horizontal
    tortuemasterpomme.end_fill()

    #Position du M
    
    tortuemasterpomme.up()
    tortuemasterpomme.forward(72*t)
    tortuemasterpomme.left(90)
    tortuemasterpomme.backward(20*t)
    tortuemasterpomme.down()
    
    i=1.2
    #Traçage du M en noir rempli de blanc
    
    tortuemasterpomme.pencolor('white')
    tortuemasterpomme.fillcolor('black')
    tortuemasterpomme.begin_fill()
    tortuemasterpomme.forward(130*i*t) #trait vers le haut
    tortuemasterpomme.left(90)
    tortuemasterpomme.forward(40*i*t) # trait horizontal
    tortuemasterpomme.left(40)
    tortuemasterpomme.forward(55*i*t) #trait cochi
    tortuemasterpomme.right(83)
    tortuemasterpomme.forward(55*i*t) #trait cochi
    tortuemasterpomme.left(42)
    tortuemasterpomme.forward(40*i*t) #trait horizontal
    tortuemasterpomme.left(90)
    tortuemasterpomme.forward(130*i*t) #trait vers le bas
    tortuemasterpomme.left(90)
    tortuemasterpomme.forward(40*i*t) #trait horizontal
    tortuemasterpomme.left(90)
    tortuemasterpomme.forward(75*i*t) #ti trait vertical
    tortuemasterpomme.right(135)
    tortuemasterpomme.forward(55*i*t) #trait cochi
    tortuemasterpomme.left(85)
    tortuemasterpomme.forward(55*i*t) #trait cochi
    tortuemasterpomme.right(129)
    tortuemasterpomme.forward(75*i*t) #ti trait vertical
    tortuemasterpomme.left(90)
    tortuemasterpomme.forward(40*i*t)  #trait horizontal
    tortuemasterpomme.end_fill()
    
    #Position tige
    tortuemasterpomme.up()
    tortuemasterpomme.backward(80*t)
    tortuemasterpomme.right(90)
    tortuemasterpomme.backward(300*t)
    tortuemasterpomme.right(90)
    tortuemasterpomme.down()
    
    #La tige verte
    tortuemasterpomme.right(90)
    tortuemasterpomme.width(3*t)
    tortuemasterpomme.pencolor('black')
    tortuemasterpomme.fillcolor('green')
    tortuemasterpomme.begin_fill()
    tortuemasterpomme.circle(15*t,180)
    tortuemasterpomme.forward(100*t)
    tortuemasterpomme.circle(15*t,180)
    tortuemasterpomme.forward(100*t)
    tortuemasterpomme.end_fill()

    #Position feuille
    tortuemasterpomme.up()
    tortuemasterpomme.backward(75*t)
    tortuemasterpomme.right(90)
    tortuemasterpomme.forward(10*t)
    tortuemasterpomme.down()

    #Feuille1
    tortuemasterpomme.right(30)
    tortuemasterpomme.fillcolor('green')
    tortuemasterpomme.begin_fill()
    tortuemasterpomme.circle(75*t,100)
    tortuemasterpomme.circle(20*t,60)
    tortuemasterpomme.circle(20*t,60)
    tortuemasterpomme.circle(112.5*t,57)
    tortuemasterpomme.end_fill()

    #Position feuille2
    tortuemasterpomme.up()
    tortuemasterpomme.right(70)
    tortuemasterpomme.forward(50*t)
    tortuemasterpomme.right(30)
    tortuemasterpomme.down()

    #Feuille2
    tortuemasterpomme.left(70)
    tortuemasterpomme.fillcolor('green')
    tortuemasterpomme.begin_fill()
    tortuemasterpomme.circle(-75*t,100)
    tortuemasterpomme.circle(-20*t,60)
    tortuemasterpomme.circle(-20*t,60)
    tortuemasterpomme.circle(-112.5*t,57)
    tortuemasterpomme.end_fill()
    tortuemasterpomme.up()
    tortuemasterpomme.goto(600,600)
    update()





