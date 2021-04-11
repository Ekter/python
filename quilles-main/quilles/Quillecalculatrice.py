from setup import *
from touche import touche


def calculatrice(taille,x,y,angle=0):
    tortuecalculatrice=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuecalculatrice)

    t=taille/8

    tracer(0)

    #Contour de la calculatrice
    tortuecalculatrice.width(2*t)
    tortuecalculatrice.pencolor('black')

    tortuecalculatrice.fillcolor('#6E8FC2')
    tortuecalculatrice.begin_fill()
    for i in range (2):
        tortuecalculatrice.forward(255*t)
        tortuecalculatrice.circle(30*t,90)
        tortuecalculatrice.forward(350*t)
        tortuecalculatrice.circle(30*t,90)
    tortuecalculatrice.end_fill()

    
    tortuecalculatrice.up()
    tortuecalculatrice.left(90)
    tortuecalculatrice.forward(60*t)
    tortuecalculatrice.down()

    #Grosse touche "−"
    
    tortuecalculatrice.width(2*t)
    tortuecalculatrice.pencolor('#900C3F')
    tortuecalculatrice.fillcolor('#354B6C')
    tortuecalculatrice.right(90)
    touche(tortuecalculatrice,120*t,32*t,5*t,"−",30*t)
   
    tortuecalculatrice.up()
    tortuecalculatrice.forward(140*t)
    tortuecalculatrice.down()

    #ti touche "0" 
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,50*t,32*t,5*t,"0",20*t)

    #touche  "3,6,9"
    dictt={0:"3",1:"6",2:"9"}
    for i in range (3):
        
        tortuecalculatrice.up()
        tortuecalculatrice.left(90)
        tortuecalculatrice.forward(52*t)
        tortuecalculatrice.right(90)
        tortuecalculatrice.down()
        touche(tortuecalculatrice,50*t,32*t,5*t,dictt.get(i),20*t)
  
    tortuecalculatrice.end_fill()


    tortuecalculatrice.up()
    tortuecalculatrice.backward(70*t)
    tortuecalculatrice.left(90)
    tortuecalculatrice.forward(52*t)
    tortuecalculatrice.right(90)
    tortuecalculatrice.down()

    
   
    idict={0:"8",1:"5",2:"2"}
    for i in range (3):
    
        tortuecalculatrice.up()
        tortuecalculatrice.right(90)
        tortuecalculatrice.forward(52*t)
        tortuecalculatrice.left(90)
        tortuecalculatrice.down()
        tortuecalculatrice.begin_fill()
        touche(tortuecalculatrice,50*t,32*t,5*t,idict.get(i),20*t)
        tortuecalculatrice.end_fill()

    
    tortuecalculatrice.up()
    tortuecalculatrice.backward(70*t)
    tortuecalculatrice.right(90)
    tortuecalculatrice.forward(52*t)
    tortuecalculatrice.left(90)
    tortuecalculatrice.down()

    di={0:"1",1:"4",2:"7"}

    for i in range (3):
        tortuecalculatrice.up()
        tortuecalculatrice.left(90)
        tortuecalculatrice.forward(52*t)
        tortuecalculatrice.right(90)
        tortuecalculatrice.down()
        tortuecalculatrice.begin_fill()
        touche(tortuecalculatrice,50*t,32*t,5*t,di.get(i),20*t)
        tortuecalculatrice.end_fill()

    tortuecalculatrice.up()
    tortuecalculatrice.forward(210*t)
    tortuecalculatrice.down()
    
    #Touche +
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,50*t,32*t,5*t,"+",20*t)
    tortuecalculatrice.end_fill()

    tortuecalculatrice.up()
    tortuecalculatrice.right(90)
    tortuecalculatrice.forward(52*t)
    tortuecalculatrice.left(90)
    tortuecalculatrice.down()
    
    #Touche *
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,50*t,32*t,5*t,"*",20*t)
    tortuecalculatrice.end_fill()
    
    tortuecalculatrice.up()
    tortuecalculatrice.backward(2.5*t)
    tortuecalculatrice.right(90)
    tortuecalculatrice.forward(20*t)
    tortuecalculatrice.down()
    
    #Touche =
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,82*t,50*t,5*t,"=",20*t,9*t)
    tortuecalculatrice.end_fill()
        
    tortuecalculatrice.up()
    tortuecalculatrice.backward(128*t)
    tortuecalculatrice.left(90)
    tortuecalculatrice.forward(20*t)
    tortuecalculatrice.down()

    #Touche ON
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,30*t,5*t,5*t,"on",8*t,3*t)
    tortuecalculatrice.end_fill()
    
    tortuecalculatrice.up()
    tortuecalculatrice.backward(45*t)
    tortuecalculatrice.down()

    #Touche OFF
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,30*t,5*t,5*t,"off",8*t,3*t)
    tortuecalculatrice.end_fill()
    
    tortuecalculatrice.up()
    tortuecalculatrice.forward(75*t)
    tortuecalculatrice.left(90)
    tortuecalculatrice.forward(30*t)
    tortuecalculatrice.down()

    #Ecran
    tortuecalculatrice.fillcolor('#8AEC84') #COuleur verte clair
    tortuecalculatrice.begin_fill()
    touche(tortuecalculatrice,60*t,250*t,5*t,"")
    tortuecalculatrice.end_fill()


    tortuecalculatrice.up()
    tortuecalculatrice.left(90)
    tortuecalculatrice.forward(70*t)
    tortuecalculatrice.down()
    
    #37
    tortuecalculatrice.pencolor('#019CDA') 
    tortuecalculatrice.write("37", font=("Arial", int(28*t), "normal"))

    tortuecalculatrice.up()
    tortuecalculatrice.backward(70*t)
    tortuecalculatrice.right(90)
    tortuecalculatrice.down()

    #Ombre écran
    tortuecalculatrice.pencolor('black')
    tortuecalculatrice.fillcolor('#047F4A') #Couleur vert foncé
    tortuecalculatrice.begin_fill()
    tortuecalculatrice.forward(60*t)
    tortuecalculatrice.left(45)
    tortuecalculatrice.forward(5*t)
    tortuecalculatrice.left(45)
    tortuecalculatrice.forward(250*t)
    tortuecalculatrice.left(45)
    tortuecalculatrice.forward(5*t)
    tortuecalculatrice.left(45)
    tortuecalculatrice.forward(10*t)
    tortuecalculatrice.left(90)
    tortuecalculatrice.pencolor('#047F4A')
    tortuecalculatrice.forward (240*t)
    tortuecalculatrice.right(90)
    tortuecalculatrice.forward(55*t)  
    tortuecalculatrice.end_fill()
    
    update()
    

