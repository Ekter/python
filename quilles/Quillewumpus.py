from turtle import begin_poly, forward
from setup import *

def wumpus(ecran,taille,x,y,angle=0):
    tortuewumpus=Turtle(undobuffersize=0,visible=False,shape="square")
    wumpus = Shape("compound")

    setup(x,y,angle,tortuewumpus)
    t=taille/8

    tracer(0)

    tortuewumpus.width(3*t)
    tortuewumpus.up()
    tortuewumpus.backward(t*88)
    tortuewumpus.left(90)
    tortuewumpus.forward(t*12)
    tortuewumpus.left(90)
    tortuewumpus.down()

    #Corps du wumpus
    tortuewumpus.fillcolor('#90a1e7')
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*47,90)
    tortuewumpus.forward(t*112)
    tortuewumpus.circle(t*14,180)
    tortuewumpus.forward(t*24)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*56)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*23)
    tortuewumpus.circle(t*14,180)
    tortuewumpus.forward(t*23)
    tortuewumpus.right(90)
    tortuewumpus.backward(t*30)
    tortuewumpus.forward(t*83)
    tortuewumpus.left(180)
    tortuewumpus.circle(t*-14,90)
    tortuewumpus.forward(t*40)
    tortuewumpus.up()
    tortuewumpus.forward(t*40)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()
    tortuewumpus.left(180)
    tortuewumpus.fillcolor('#abbaf1')
    #Pelage avant
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*80)
    tortuewumpus.circle(t*13,90)
    tortuewumpus.right(90)
    tortuewumpus.down()
    tortuewumpus.forward(t*25)
    tortuewumpus.circle(t*14,180)
    tortuewumpus.forward(t*25)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*37)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*25)
    tortuewumpus.circle(t*14,180)
    tortuewumpus.forward(t*25)
    tortuewumpus.right(90)
    tortuewumpus.circle(t*20,90)
    tortuewumpus.forward(t*60)
    tortuewumpus.up()
    tortuewumpus.forward(t*20)
    tortuewumpus.down()
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()
    tortuewumpus.backward(t*22)
    tortuewumpus.down()

    #Contour de la tête
    tortuewumpus.begin_poly()
    tortuewumpus.right(90)
    tortuewumpus.forward(t*20)
    tortuewumpus.circle(t*44,90)
    tortuewumpus.forward(t*13)
    tortuewumpus.up()
    tortuewumpus.forward(t*83)
    tortuewumpus.down()
    tortuewumpus.circle(t*44,90)
    tortuewumpus.forward(t*142)
    tortuewumpus.circle(t*44,65)
    tortuewumpus.up()
    tortuewumpus.circle(t*44,25)
    tortuewumpus.forward(t*66)
    tortuewumpus.down()
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*44,90)
    tortuewumpus.forward(t*142)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()
    tortuewumpus.circle(t*44,90)
    tortuewumpus.forward(t*96)
    tortuewumpus.circle(t*44,90)
    tortuewumpus.forward(t*142)
    tortuewumpus.down()

    #Arrière de la tête
    tortuewumpus.fillcolor('#90a1e7')
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*44,65)
    tortuewumpus.up()
    tortuewumpus.circle(t*44,25)
    tortuewumpus.forward(t*66)
    tortuewumpus.down()
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*44,90)
    tortuewumpus.forward(t*30)
    tortuewumpus.up()
    tortuewumpus.left(180)
    tortuewumpus.circle(t*-44,90)
    tortuewumpus.forward(t*96)
    tortuewumpus.circle(t*-44,90)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    #Oeil
    tortuewumpus.forward(t*35)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*80)
    
    a,b=tortuewumpus.pos()
    tortuewumpus.forward(12.5*t)
    tortuewumpus.down()
    tortuewumpus.right(90)
    tortuewumpus.begin_poly()
    tortuewumpus.circle(-12.5*t)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())
    tortuewumpus.left(90)
    tortuewumpus.up()
    tortuewumpus.backward(t*53)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*62)
    tortuewumpus.down()

    #Oreille
    tortuewumpus.fillcolor('#abbaf1')
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*50)
    tortuewumpus.circle(t*30,90)
    tortuewumpus.forward(t*20)
    tortuewumpus.circle(t*30,90)
    tortuewumpus.forward(t*50)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()
    tortuewumpus.left(90)
    tortuewumpus.forward(t*66)
    tortuewumpus.left(90)
    tortuewumpus.down()

    #Interieur de l'oreille
    tortuewumpus.fillcolor('#90a1e7')
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*50)
    tortuewumpus.circle(t*15,90)
    tortuewumpus.forward(t*25)
    tortuewumpus.circle(t*15,90)
    tortuewumpus.forward(t*30)
    tortuewumpus.up()
    tortuewumpus.forward(t*20)
    tortuewumpus.down()
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())
    
    tortuewumpus.up()
    tortuewumpus.forward(t*135)
    tortuewumpus.left(90)
    tortuewumpus.forward(t*50)
    tortuewumpus.right(90)
    tortuewumpus.down()

    #Contour museau
    tortuewumpus.fillcolor('#c9d5f1')
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*80)
    tortuewumpus.circle(t*-20,90)
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*-35,90)
    tortuewumpus.forward(t*50)
    tortuewumpus.circle(t*-35,90)
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*-20,90)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    #Relief de son museau
    tortuewumpus.fillcolor('#b4c8f4')
    tortuewumpus.begin_poly()
    tortuewumpus.left(180)
    tortuewumpus.forward(t*20)
    tortuewumpus.circle(t*20,90)
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*35,90)
    tortuewumpus.forward(t*20)
    tortuewumpus.left(180)
    tortuewumpus.circle(t*-35,90)
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*-20,90)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()
    tortuewumpus.forward(t*16)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*50)
    tortuewumpus.left(90)
    tortuewumpus.down()

    #Trou de narine
    tortuewumpus.fillcolor('#a8b7ed')
    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*23)
    tortuewumpus.circle(t*-8,180)
    tortuewumpus.forward(t*23)
    tortuewumpus.circle(t*-8,180)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()
    tortuewumpus.forward(t*50)
    tortuewumpus.down()

    tortuewumpus.begin_poly()
    tortuewumpus.forward(t*10)
    tortuewumpus.circle(t*-8,180)
    tortuewumpus.forward(t*10)
    tortuewumpus.circle(t*-8,180)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    tortuewumpus.up()   
    tortuewumpus.backward(t*40)
    tortuewumpus.right(90)
    tortuewumpus.forward(t*54)
    tortuewumpus.left(90)
    tortuewumpus.down()
    tortuewumpus.forward(t*30)
    
    tortuewumpus.up()
    tortuewumpus.backward(t*334)
    tortuewumpus.left(90)
    tortuewumpus.forward(t*12)
    tortuewumpus.down()

    #Queue
    tortuewumpus.fillcolor('#abbaf1')
    tortuewumpus.begin_poly()
    tortuewumpus.left(10)
    tortuewumpus.forward(t*30)
    tortuewumpus.circle(t*24,250)
    tortuewumpus.forward(t*33)
    tortuewumpus.end_poly()
    wumpus.addcomponent(tortuewumpus.get_poly(),tortuewumpus.fillcolor(),tortuewumpus.pencolor())

    
    ecran.addshape('wumpus', shape=wumpus)
