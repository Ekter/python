from setup import *
from quatredeux import quatredeux

def livreqd(taille,x,y,angle=0,texte=0,couleur='red'):

    tortuelivreqd=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuelivreqd)

    t=taille/7

    tracer(0)
    tortuelivreqd.width(3*t)
    
    tortuelivreqd.up()
    tortuelivreqd.backward(t*115)
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*152)
    tortuelivreqd.left(98)
    tortuelivreqd.down()


    #Couverture du livre
    tortuelivreqd.fillcolor(couleur)
    tortuelivreqd.begin_fill()
    for i in range(2):
        tortuelivreqd.forward(t*185)
        tortuelivreqd.left(82)
        tortuelivreqd.forward(t*300)
        tortuelivreqd.left(98)
    tortuelivreqd.end_fill()
    
    #Dessous du livre
    tortuelivreqd.setheading(0)
    tortuelivreqd.left(90)
    tortuelivreqd.begin_fill()
    tortuelivreqd.forward(t*300)
    tortuelivreqd.left(135)
    tortuelivreqd.forward(t*17)
    tortuelivreqd.left(45)
    tortuelivreqd.forward(t*290)
    tortuelivreqd.circle(t*20,90)
    tortuelivreqd.forward(t*232)
    tortuelivreqd.left(90)
    tortuelivreqd.forward(t*300)
    tortuelivreqd.left(90)
    tortuelivreqd.forward(t*20)
    tortuelivreqd.left(135)
    tortuelivreqd.forward(t*10)
    tortuelivreqd.right(45)
    tortuelivreqd.forward(t*282)
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*210)
    tortuelivreqd.left(90)
    tortuelivreqd.forward(t*10)
    tortuelivreqd.backward(t*10)
    tortuelivreqd.right(90)
    tortuelivreqd.circle(t*-20,60)
    tortuelivreqd.end_fill()
    
    tortuelivreqd.setheading(0)
    tortuelivreqd.fillcolor('white')
    tortuelivreqd.begin_fill()
    tortuelivreqd.left(8)
    tortuelivreqd.forward(t*185)
    tortuelivreqd.left(82)
    tortuelivreqd.forward(t*265)
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*25)
    r,c=tortuelivreqd.pos()
    tortuelivreqd.right(45)
    tortuelivreqd.forward(t*27)
    tortuelivreqd.right(45)
    tortuelivreqd.forward(t*282)
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*210)
    tortuelivreqd.circle(t*-20,60)
    tortuelivreqd.end_fill()

    tortuelivreqd.up()
    tortuelivreqd.setheading(0)
    tortuelivreqd.goto(r,c)
    tortuelivreqd.down()
    
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*290)
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*190)

    tortuelivreqd.up()
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*200)
    tortuelivreqd.right(90)
    tortuelivreqd.forward(t*50)
    tortuelivreqd.down()
    quatredeux(30*t,5*t,tortuelivreqd)
    
    
    update()
