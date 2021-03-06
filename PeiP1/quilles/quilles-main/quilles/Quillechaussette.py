from setup import *
def chaussette(taille,x,y,angle=0):

    tortuechaussette=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuechaussette)

    t=taille/4

    tracer(0)

    tortuechaussette.up()
    tortuechaussette.forward(t*-20)
    tortuechaussette.right(80)
    tortuechaussette.down()

    tortuechaussette.fillcolor('#ffca39')
    tortuechaussette.begin_fill()
    tortuechaussette.forward(t*50)
    tortuechaussette.circle(t*-18,90)
    tortuechaussette.circle(t*-70,20)
    tortuechaussette.circle(t*70,30)
    tortuechaussette.circle(t*30,160)
    tortuechaussette.circle(t*600,12)
    tortuechaussette.circle(t*30,90)
    tortuechaussette.forward(t*145)
    tortuechaussette.left(80)
    tortuechaussette.forward(t*70)
    tortuechaussette.left(96)
    tortuechaussette.forward(t*90)
    tortuechaussette.end_fill()

    tortuechaussette.up()
    tortuechaussette.left(5)
    tortuechaussette.forward(t*15)
    tortuechaussette.circle(t*-18,90)
    tortuechaussette.circle(t*-70,20)
    tortuechaussette.circle(t*70,30)
    tortuechaussette.fillcolor('#18850a')
    tortuechaussette.begin_fill()
    tortuechaussette.circle(t*30,160)
    jk,lm=tortuechaussette.pos()
    tortuechaussette.down()
    tortuechaussette.left(50)
    tortuechaussette.circle(t*35,110)
    tortuechaussette.end_fill()

    tortuechaussette.up()
    tortuechaussette.goto(jk,lm)
    tortuechaussette.right(160)
    tortuechaussette.down()
    tortuechaussette.right(2)
    tortuechaussette.circle(t*600,7)
    tortuechaussette.fillcolor('#c25253')
    tortuechaussette.begin_fill()
    tortuechaussette.circle(t*600,5)
    tortuechaussette.circle(t*30,90)
    az,fo=tortuechaussette.pos()
    tortuechaussette.forward(t*12)
    tortuechaussette.left(70)
    tortuechaussette.circle(t*60,93)
    tortuechaussette.end_fill()
    
    tortuechaussette.up()
    tortuechaussette.goto(az,fo)
    tortuechaussette.right(163)
    tortuechaussette.forward(t*100)
    tortuechaussette.down()

    tortuechaussette.begin_fill()
    for i in range(2):
        tortuechaussette.forward(t*20)
        tortuechaussette.left(85)
        tortuechaussette.forward(t*73)
        tortuechaussette.left(95)
    tortuechaussette.end_fill()
    

    update()



