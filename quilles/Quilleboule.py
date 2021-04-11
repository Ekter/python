from setup import *
def boule(ecran,taille,x,y,angle=0):
    y+=13*taille
    tortueboule=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortueboule)
    boule = Shape("compound")

    t=taille/6

    tracer(0)

    #La boule noire
    up()
    tortueboule.right(90)
    tortueboule.backward(t*150)
    tortueboule.right(90)
    
    tortueboule.begin_poly()
    tortueboule.circle(t*200,360)
    tortueboule.end_poly()
    boule.addcomponent(tortueboule.get_poly(), "black", "black")

    #Le cercle blanc
    tortueboule.left(90)
    tortueboule.pencolor('blue')
    tortueboule.forward(t*130)
    tortueboule.right(90)

    tortueboule.fillcolor('white')
    tortueboule.begin_poly()
    tortueboule.circle(t*75,360)
    tortueboule.end_poly()
    boule.addcomponent(tortueboule.get_poly(), "white", "blue")
    ecran.addshape('boule', shape=boule)

    #Ecriture du 8
