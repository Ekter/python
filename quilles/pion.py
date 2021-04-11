from setup import *

def pion(ecran,taille,x,y,angle=0):
    tortuepion=Turtle(undobuffersize=0,visible=False,shape="square")
    pion = Shape("compound")
    setup(x,y,angle,tortuepion)

    t=taille/1.3
    width(3*t)

    tracer(0)

    tortuepion.up()
    tortuepion.left(90)
    tortuepion.forward(t*48)
    tortuepion.right(100)
    tortuepion.down()
    tortuepion.begin_poly()
    tortuepion.circle(t*44,370)
    tortuepion.end_poly()
    pion.addcomponent(tortuepion.get_poly(),"white","black")
    tortuepion.up()
    tortuepion.left(90)
    tortuepion.forward(t*3)
    tortuepion.right(90)
    tortuepion.down()

    tortuepion.begin_poly()
    tortuepion.forward(t*30)
    tortuepion.circle(t*-10,180)
    tortuepion.left(70)
    tortuepion.circle(t*103,77)
    tortuepion.right(57)
    tortuepion.forward(t*40)
    tortuepion.left(90)
    tortuepion.forward(t*9)
    tortuepion.circle(t*-10,180)
    tortuepion.forward(t*160)
    tortuepion.circle(t*-10,180)
    tortuepion.forward(t*9)
    tortuepion.left(90)
    tortuepion.forward(t*40)
    tortuepion.right(57)
    tortuepion.circle(t*103,77)
    tortuepion.left(70)
    tortuepion.circle(t*-10,180)
    tortuepion.forward(t*30)
    tortuepion.end_poly()
    pion.addcomponent(tortuepion.get_poly(),"white","black")
    
    tortuepion.up()
    tortuepion.forward(t*-30)
    tortuepion.right(90)
    tortuepion.forward(t*30)
    tortuepion.left(90)
    tortuepion.down()
    
    tortuepion.begin_poly()
    for i in range(2):
        tortuepion.forward(t*63)
        tortuepion.left(90)
        tortuepion.forward(t*13)
        tortuepion.left(90)
    tortuepion.end_poly()
    pion.addcomponent(tortuepion.get_poly(),"white","black")

    tortuepion.up()
    tortuepion.forward(t*-45)
    tortuepion.right(90)
    tortuepion.forward(t*150)
    tortuepion.left(90)
    tortuepion.down()

    tortuepion.begin_poly()
    for i in range(2):
        tortuepion.forward(t*150)
        tortuepion.circle(t*15,180)
    tortuepion.end_poly()
    pion.addcomponent(tortuepion.get_poly(),"white","black")
    ecran.addshape('pion', shape=pion)
    update()

