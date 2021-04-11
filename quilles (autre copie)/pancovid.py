from setup import *
from ici import ici
from pan import pancarte

def pancartecovid(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)
    
    pancarte(1,0,0,0,1.4,1.8)


    up()
    
    forward(150)
    left(90)
    forward(140)
    right(90)
    down()

    ici(2,1)

pancartecovid(2,0,0)

