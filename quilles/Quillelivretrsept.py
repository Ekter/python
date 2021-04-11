from setup import *
from troissept import troissept

def Livrets(taille,x,y,angle=0,texte=0,couleur='red'):
    
    tortuelivrets=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuelivrets)

    t=taille/7
    tortuelivrets.width(3*t)

    tracer(0)
    
    tortuelivrets.up()

    tortuelivrets.backward(t*115)
    tortuelivrets.right(90)
    tortuelivrets.forward(t*152)
    tortuelivrets.left(98)
    tortuelivrets.down()


    #Couverture du livre
    tortuelivrets.fillcolor(couleur)
    tortuelivrets.begin_fill()
    for i in range(2):
        tortuelivrets.forward(t*185)
        tortuelivrets.left(82)
        tortuelivrets.forward(t*300)
        tortuelivrets.left(98)
    tortuelivrets.end_fill()
    
    #Dessous du livre
    tortuelivrets.setheading(0)
    tortuelivrets.left(90)
    tortuelivrets.begin_fill()
    tortuelivrets.forward(t*300)
    tortuelivrets.left(135)
    tortuelivrets.forward(t*17)
    tortuelivrets.left(45)
    tortuelivrets.forward(t*290)
    tortuelivrets.circle(t*20,90)
    tortuelivrets.forward(t*232)
    tortuelivrets.left(90)
    tortuelivrets.forward(t*300)
    tortuelivrets.left(90)
    tortuelivrets.forward(t*20)
    tortuelivrets.left(135)
    tortuelivrets.forward(t*10)
    tortuelivrets.right(45)
    tortuelivrets.forward(t*282)
    tortuelivrets.right(90)
    tortuelivrets.forward(t*210)
    tortuelivrets.left(90)
    tortuelivrets.forward(t*10)
    tortuelivrets.backward(t*10)
    tortuelivrets.right(90)
    tortuelivrets.circle(t*-20,60)
    tortuelivrets.end_fill()
    
    tortuelivrets.setheading(0)
    tortuelivrets.fillcolor('white')
    tortuelivrets.begin_fill()
    tortuelivrets.left(8)
    tortuelivrets.forward(t*185)
    tortuelivrets.left(82)
    tortuelivrets.forward(t*265)
    tortuelivrets.right(90)
    tortuelivrets.forward(t*25)
    r,c=tortuelivrets.pos()
    tortuelivrets.right(45)
    tortuelivrets.forward(t*27)
    tortuelivrets.right(45)
    tortuelivrets.forward(t*282)
    tortuelivrets.right(90)
    tortuelivrets.forward(t*210)
    tortuelivrets.circle(t*-20,60)
    tortuelivrets.end_fill()

    tortuelivrets.up()
    tortuelivrets.setheading(0)
    tortuelivrets.goto(r,c)
    tortuelivrets.down()
    
    tortuelivrets.right(90)
    tortuelivrets.forward(t*290)
    tortuelivrets.right(90)
    tortuelivrets.forward(t*190)

    tortuelivrets.up()
    tortuelivrets.right(90)
    tortuelivrets.forward(t*200)
    tortuelivrets.right(90)
    tortuelivrets.forward(t*50)
    tortuelivrets.down()
    troissept(tortuelivrets,30*t,5*t)
    
    update()

    ht()
