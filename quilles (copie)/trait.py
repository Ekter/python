from turtle import *
def trait(miroir,nombre,taille, droite=0, gauche=0):

    t=taille
    m=miroir
    d,f=pos()

    for i in range (nombre):

        right(droite*m)
        left(gauche*m)

        left(90*m)
        a,b=pos()
        forward(7*t)

        up()
        left(droite*m)
        right(gauche*m)
        goto(a,b)
        right(90*m)
        forward(6*t)
        down()

    up()
    goto(d,f)
    down()
    
