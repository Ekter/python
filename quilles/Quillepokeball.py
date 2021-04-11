from setup import *
def pokeball(ecran,taille,x,y,angle=0):
    pokeball = Shape("compound")

    tortuepokeball=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuepokeball)
    
    t=taille/8


    tracer(0)

    tortuepokeball.width(3*t)
    tortuepokeball.up()
    tortuepokeball.forward(t*225)
    tortuepokeball.left(90)
    tortuepokeball.forward(t*8)
    tortuepokeball.right(90)
    tortuepokeball.down()
    tortuepokeball.left(268)

    tortuepokeball.fillcolor('white')
    tortuepokeball.begin_poly()
    tortuepokeball.circle(t*-218,360)
    tortuepokeball.end_poly()
    pokeball.addcomponent(tortuepokeball.get_poly(),tortuepokeball.fillcolor(),tortuepokeball.pencolor())

    tortuepokeball.fillcolor('red')
    tortuepokeball.begin_poly()
    tortuepokeball.right(55)
    tortuepokeball.circle(t*-390,68)
    tortuepokeball.right(55)
    tortuepokeball.circle(t*-218,186.5)
    tortuepokeball.end_poly()
    pokeball.addcomponent(tortuepokeball.get_poly(),tortuepokeball.fillcolor(),tortuepokeball.pencolor())

    tortuepokeball.fillcolor('black')
    tortuepokeball.begin_poly()
    tortuepokeball.right(45)
    tortuepokeball.circle(t*-270,31.5)
    tortuepokeball.left(80)
    tortuepokeball.circle(t*-70,175)
    tortuepokeball.left(85)
    tortuepokeball.circle(t*-270,36.5)
    tortuepokeball.right(44)
    tortuepokeball.circle(t*-218,10)
    tortuepokeball.right(132)
    tortuepokeball.circle(t*270,37.9)
    tortuepokeball.left(80)
    tortuepokeball.circle(t*-70,144)
    tortuepokeball.left(80)
    tortuepokeball.circle(t*270,35)
    tortuepokeball.right(130)
    tortuepokeball.circle(t*-218,10)
    tortuepokeball.end_poly()
    pokeball.addcomponent(tortuepokeball.get_poly(),tortuepokeball.fillcolor(),tortuepokeball.pencolor())

    

    tortuepokeball.up()
    tortuepokeball.right(70)
    tortuepokeball.forward(t*180)
    tortuepokeball.down()
    tortuepokeball.right(80)
    tortuepokeball.fillcolor('white')
    tortuepokeball.begin_poly()
    tortuepokeball.circle(t*36,360)
    tortuepokeball.end_poly()
    pokeball.addcomponent(tortuepokeball.get_poly(),tortuepokeball.fillcolor(),tortuepokeball.pencolor())
    ecran.addshape('pokeball', shape=pokeball)

