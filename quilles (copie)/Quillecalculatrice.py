from setup import *
from touche import touche


def Calculette(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)

    #Contour de la calculatrice
    width(2*t)
    pencolor('black')

    fillcolor('#6E8FC2')
    begin_fill()
    for i in range (2):
        forward(255*t)
        circle(30*t,90)
        forward(350*t)
        circle(30*t,90)
    end_fill()

    
    up()
    left(90)
    forward(60*t)
    down()

    #Grosse touche "−"
    
    width(2*t)
    pencolor('#900C3F')
    fillcolor('#354B6C')
    right(90)
    touche(120*t,32*t,5*t,"−",30*t)
   
    up()
    forward(140*t)
    down()

    #ti touche "0" 
    begin_fill()
    touche(50*t,32*t,5*t,"0",20*t)

    #touche  "3,6,9"
    dictt={0:"3",1:"6",2:"9"}
    for i in range (3):
        
        up()
        left(90)
        forward(52*t)
        right(90)
        down()
        touche(50*t,32*t,5*t,dictt.get(i),20*t)
  
    end_fill()


    up()
    backward(70*t)
    left(90)
    forward(52*t)
    right(90)
    down()

    
   
    idict={0:"8",1:"5",2:"2"}
    for i in range (3):
    
        up()
        right(90)
        forward(52*t)
        left(90)
        down()
        begin_fill()
        touche(50*t,32*t,5*t,idict.get(i),20*t)
        end_fill()

    
    up()
    backward(70*t)
    right(90)
    forward(52*t)
    left(90)
    down()

    di={0:"1",1:"4",2:"7"}

    for i in range (3):
        up()
        left(90)
        forward(52*t)
        right(90)
        down()
        begin_fill()
        touche(50*t,32*t,5*t,di.get(i),20*t)
        end_fill()

    up()
    forward(210*t)
    down()
    
    #Touche +
    begin_fill()
    touche(50*t,32*t,5*t,"+",20*t)
    end_fill()

    up()
    right(90)
    forward(52*t)
    left(90)
    down()
    
    #Touche *
    begin_fill()
    touche(50*t,32*t,5*t,"*",20*t)
    end_fill()
    
    up()
    backward(2.5*t)
    right(90)
    forward(20*t)
    down()
    
    #Touche =
    begin_fill()
    touche(82*t,50*t,5*t,"=",20*t,9*t)
    end_fill()
        
    up()
    backward(128*t)
    left(90)
    forward(20*t)
    down()

    #Touche ON
    begin_fill()
    touche(30*t,5*t,5*t,"on",8*t,3*t)
    end_fill()
    
    up()
    backward(45*t)
    down()

    #Touche OFF
    begin_fill()
    touche(30*t,5*t,5*t,"off",8*t,3*t)
    end_fill()
    
    up()
    forward(75*t)
    left(90)
    forward(30*t)
    down()

    #Ecran
    fillcolor('#8AEC84') #COuleur verte clair
    begin_fill()
    touche(60*t,250*t,5*t,"")
    end_fill()


    up()
    left(90)
    forward(70*t)
    down()
    
    #37
    pencolor('#019CDA') 
    write("37", font=("Arial", int(28*t), "normal"))

    up()
    backward(70*t)
    right(90)
    down()

    #Ombre écran
    pencolor('black')
    fillcolor('#047F4A') #Couleur vert foncé
    begin_fill()
    forward(60*t)
    left(45)
    forward(5*t)
    left(45)
    forward(250*t)
    left(45)
    forward(5*t)
    left(45)
    forward(10*t)
    left(90)
    pencolor('#047F4A')
    forward (240*t)
    right(90)
    forward(55*t)  
    end_fill()
    
    update()
    
