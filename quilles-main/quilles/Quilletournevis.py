from setup import *

def tournevis (taille,x,y,angle=0):
    
    t=taille/8

    tortuetournevis=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuetournevis)

    tracer(0)

    tortuetournevis.up()
    tortuetournevis.width(3*t)
    tortuetournevis.left(57)
    tortuetournevis.left(90)
    tortuetournevis.forward(t*9)
    tortuetournevis.right(90)
    tortuetournevis.down()

    tortuetournevis.right(10)

    tortuetournevis.fillcolor('#9bd9e5')
    for i in range(2):
        tortuetournevis.forward(t*16)
        tortuetournevis.right(90)
        tortuetournevis.forward(t*33)
        tortuetournevis.right(90)
    tortuetournevis.up()
    tortuetournevis.forward(t*16)
    tortuetournevis.right(90)
    tortuetournevis.forward(t*9)
    tortuetournevis.left(90)
    tortuetournevis.down()

    tortuetournevis.fillcolor('#c5d3da')
    tortuetournevis.begin_fill()
    tortuetournevis.forward(t*210)
    tortuetournevis.left(20)
    tortuetournevis.forward(t*10)
    tortuetournevis.right(25)
    tortuetournevis.forward(t*40)
    tortuetournevis.right(85)
    tortuetournevis.forward(t*15)
    tortuetournevis.right(85)
    tortuetournevis.forward(t*40)
    tortuetournevis.right(25)
    tortuetournevis.forward(t*10)
    tortuetournevis.left(20)
    tortuetournevis.forward(t*210)
    tortuetournevis.right(90)
    tortuetournevis.end_fill()

    tortuetournevis.up()
    tortuetournevis.forward(t*40)
    tortuetournevis.left(90)
    tortuetournevis.forward(t*50)
    tortuetournevis.down()
    tortuetournevis.fillcolor('#3686c8') 
    tortuetournevis.begin_fill()
    for i in range(2):
        tortuetournevis.forward(t*210)
        tortuetournevis.circle(t*32,180)
    tortuetournevis.end_fill()

    tortuetournevis.up()
    tortuetournevis.forward(t*10)
    tortuetournevis.left(90)
    tortuetournevis.forward(t*-12)
    tortuetournevis.right(90)
    tortuetournevis.down()

    tortuetournevis.fillcolor('#6ac188')
    tortuetournevis.begin_fill()
    for i in range(2):
        tortuetournevis.up()
        tortuetournevis.left(90)
        tortuetournevis.forward(t*25)
        tortuetournevis.right(90)
        tortuetournevis.down()


        for i in range(2):
            tortuetournevis.forward(t*190)
            tortuetournevis.circle(t*7,180)

    tortuetournevis.end_fill()
            

    tortuetournevis.up()
    tortuetournevis.forward(t*-20)
    tortuetournevis.left(90)
    tortuetournevis.forward(t*20)
    tortuetournevis.down()

    tortuetournevis.fillcolor('#9bd9e5')
    tortuetournevis.begin_fill()
    for i in range(2):
       tortuetournevis.left(90)
       tortuetournevis.forward(t*25)
       tortuetournevis.left(90)
       tortuetournevis.forward(t*50)
    tortuetournevis.end_fill()

    update()
