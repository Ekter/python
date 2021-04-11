from turtle import *
def trait(tortue,miroir,nombre,taille, droite=0, gauche=0,exeption=0):

    t=taille
    m=miroir
    d,f=tortue.pos()

    for i in range (nombre):

        tortue.right(droite+(90-90*m)*exeption)#droite*m)
        tortue.left(gauche*m)
        tortue.left(90*m)
        a,b=tortue.pos()
        tortue.forward(7*t)
        tortue.up()
        tortue.left(droite*m)
        tortue.right(gauche*m)
        tortue.goto(a,b)
        tortue.right(90*m+(-90+90*m)*exeption)
        tortue.forward(6*t)
        tortue.down()

    tortue.up()
    tortue.goto(d,f)
    tortue.down()
    
