from setup import *
def masque(ecran,taille,x,y,angle=0):
    masque = Shape("compound")

    tortuemasque=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuemasque)
    
    t=taille/6

    tracer(0)

    tortuemasque.width(2*t)
    tortuemasque.pencolor('black')
    tortuemasque.fillcolor('#c5e2f3')
    
    tortuemasque.up()
    tortuemasque.backward(t*145)
    tortuemasque.left(90)
    tortuemasque.forward(t*90)
    tortuemasque.right(110)
    tortuemasque.down()

    #Couvrebouche    
    tortuemasque.begin_poly()
    tortuemasque.circle(t*440,37.5)
    tortuemasque.right(105)
    tortuemasque.forward(t*150)
    tortuemasque.right(65)
    tortuemasque.circle(t*-310,55.6)
    tortuemasque.right(61)
    tortuemasque.forward(t*151)
    tortuemasque.end_poly()
    masque.addcomponent(tortuemasque.get_poly(),tortuemasque.fillcolor(),tortuemasque.pencolor())

    tortuemasque.up()
    tortuemasque.backward(t*40)
    tortuemasque.right(90)
    tortuemasque.forward(t*30)
    tortuemasque.right(25)
    u,n=tortuemasque.pos()
    tortuemasque.down()

    #Pli de masque
    for i in range (20):
        tortuemasque.width(t*(2+0.1*i))
        tortuemasque.circle(t*350,1)

    tortuemasque.left(6)

    for i in range(20):
        tortuemasque.width(t*(4-0.1*i))
        tortuemasque.circle(t*350,1)

    tortuemasque.up()
    tortuemasque.goto(u,n)
    tortuemasque.right(120)
    tortuemasque.forward(t*15)
    tortuemasque.left(75)
    tortuemasque.down()
    

    for i in range (20):
        tortuemasque.width(t*(2+0.1*i))
        tortuemasque.circle(t*350,1)

    tortuemasque.left(6)

    for i in range(20):
        tortuemasque.width(t*(4-0.1*i))
        tortuemasque.circle(t*350,1)

    tortuemasque.up()
    tortuemasque.goto(u,n)
    tortuemasque.right(120)
    tortuemasque.forward(t*55)
    tortuemasque.left(73)
    tortuemasque.down()

    for i in range (20):
        tortuemasque.width(t*(2+0.1*i))
        tortuemasque.circle(t*350,1)

    tortuemasque.left(6)

    for i in range(20):
        tortuemasque.width(t*(4-0.1*i))
        tortuemasque.circle(t*350,1)

    tortuemasque.up()
    tortuemasque.forward(t*20)
    tortuemasque.right(70)
    tortuemasque.forward(t*15)
    tortuemasque.left(73)
    tortuemasque.down()

    #Les deux languettes

    tortuemasque.fillcolor('#cbc4ba')
    tortuemasque.begin_poly()
    tortuemasque.circle(t*300,14)
    tortuemasque.circle(t*57,116)
    tortuemasque.left(50)
    tortuemasque.forward(t*60)
    tortuemasque.right(110)
    tortuemasque.forward(t*15)
    tortuemasque.right(70)
    tortuemasque.forward(t*50)
    tortuemasque.right(25)
    tortuemasque.circle(t*-60,130)
    tortuemasque.left(6)
    tortuemasque.circle(t*-134,30)
    tortuemasque.forward(t*35)
    tortuemasque.right(110)
    tortuemasque.forward(t*15)
    tortuemasque.end_poly()
    masque.addcomponent(tortuemasque.get_poly(),tortuemasque.fillcolor(),tortuemasque.pencolor())
    
    tortuemasque.up()
    tortuemasque.left(84)
    tortuemasque.forward(t*288)
    tortuemasque.left(90)
    tortuemasque.forward(t*16)
    tortuemasque.right(90)
    tortuemasque.down()

    tortuemasque.begin_poly()
    tortuemasque.right(23)
    tortuemasque.circle(t*-300,17)
    tortuemasque.left(5)
    tortuemasque.circle(t*-63,138)
    tortuemasque.right(30)
    tortuemasque.forward(t*50)
    tortuemasque.right(74)
    tortuemasque.forward(t*14)
    tortuemasque.right(110)
    tortuemasque.forward(t*50)
    tortuemasque.left(50)
    tortuemasque.circle(t*60,130)
    tortuemasque.right(6)
    tortuemasque.circle(t*134,10)
    tortuemasque.left(5)
    tortuemasque.forward(t*32)
    tortuemasque.right(82)
    tortuemasque.forward(t*20)
    tortuemasque.end_poly()
    masque.addcomponent(tortuemasque.get_poly(),tortuemasque.fillcolor(),tortuemasque.pencolor())
    ecran.addshape('masque', shape=masque)
