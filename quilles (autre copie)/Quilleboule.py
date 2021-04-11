from setup import *
def boule(taille,x,y,angle=0):
    y+=13*taille
    tortueboule=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortueboule)

    t=taille/6

    tracer(0)

    #La boule noire
    up()
    tortueboule.right(90)
    tortueboule.backward(t*150)
    tortueboule.right(90)
    
    tortueboule.begin_fill()
    tortueboule.circle(t*200,360)
    tortueboule.end_fill()

    #Le cercle blanc
    tortueboule.left(90)
    tortueboule.pencolor('blue')
    tortueboule.forward(t*130)
    tortueboule.right(90)

    tortueboule.fillcolor('white')
    tortueboule.begin_fill()
    tortueboule.circle(t*75,360)
    tortueboule.end_fill()

    #Ecriture du 8

    tortueboule.left(90)
    tortueboule.forward(t*145)
    tortueboule.right(90)
    tortueboule.forward(t*30)

    tortueboule.write('8', font=("Arial",int(90*t), "normal"))

    update()
