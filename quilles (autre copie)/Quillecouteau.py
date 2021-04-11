from setup import *
def couteau(taille,x,y,angle=0):

    tortuecouteau=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuecouteau)

    t=taille/10

    tracer(0)

    tortuecouteau.width(7*t)
    tortuecouteau.pencolor('black')

    #Lame du couteau
    tortuecouteau.fillcolor('grey')
    tortuecouteau.begin_fill()
    tortuecouteau.left(41)
    for i in range (6):
        
        tortuecouteau.width(7*t)
        tortuecouteau.forward(t*21)
        a,z=tortuecouteau.pos()
        tortuecouteau.right(90)
        tortuecouteau.width(5*t)
        tortuecouteau.forward(t*20)
        tortuecouteau.left(90)
        tortuecouteau.goto(a,z)
        
    tortuecouteau.width(7*t)
    tortuecouteau.forward(t*160)
    tortuecouteau.right(10)
    tortuecouteau.forward(t*137)
    tortuecouteau.right(110)
    tortuecouteau.circle(t*-180,60)
    tortuecouteau.forward(t*225)
    tortuecouteau.width(9*t)
    tortuecouteau.left(45)
    tortuecouteau.forward(t*10)
    tortuecouteau.right(45)
    e,r=tortuecouteau.pos()
    tortuecouteau.width(8*t)
    tortuecouteau.forward(t*23)
    tortuecouteau.right(90)
    tortuecouteau.forward(t*25)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*15)
    tortuecouteau.right(90)
    tortuecouteau.width(15*t)
    tortuecouteau.forward(t*150)
    tortuecouteau.end_fill()

    #Haut du manche
    tortuecouteau.fillcolor('#3E3E3C')
    tortuecouteau.begin_fill()
    tortuecouteau.width(9*t)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*30)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*190)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*30)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*35)

    tortuecouteau.end_fill()

    tortuecouteau.up()
    tortuecouteau.forward(t*5)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*35)
    tortuecouteau.down()

    tortuecouteau.right(40)
    tortuecouteau.circle(t*36,90)
    tortuecouteau.right(100)
    tortuecouteau.circle(t*36,95)
    tortuecouteau.right(100)
    tortuecouteau.circle(t*36,95)
    tortuecouteau.right(80)
    tortuecouteau.circle(t*36,90)

    #Bas du manche
    tortuecouteau.fillcolor('#9B937A')
    tortuecouteau.begin_fill()
    tortuecouteau.circle(t*36,30)
    tortuecouteau.circle(t*-6,180)
    tortuecouteau.left(40)

    tortuecouteau.circle(t*-110,60)
    tortuecouteau.right(55)
    tortuecouteau.circle(t*-50,30)
    tortuecouteau.width(2*t)
    tortuecouteau.right(90)
    tortuecouteau.circle(t*140,40)
    tortuecouteau.end_fill()

    #Manche
    tortuecouteau.fillcolor('#34322A')
    tortuecouteau.begin_fill()
    tortuecouteau.left(180)
    tortuecouteau.circle(t*-140,40)
    tortuecouteau.width(9*t)
    tortuecouteau.right(80)
    tortuecouteau.circle(t*100,30)
    tortuecouteau.circle(t*-150,30)
    tortuecouteau.circle(t*120,30)
    j,k=tortuecouteau.pos()
    tortuecouteau.right(105)
    tortuecouteau.width(8*t)
    tortuecouteau.forward(t*90)
    tortuecouteau.right(110)
    tortuecouteau.circle(t*36,70)
    tortuecouteau.right(100)
    tortuecouteau.circle(t*36,95)
    tortuecouteau.right(100)
    tortuecouteau.circle(t*36,95)
    tortuecouteau.right(80)
    tortuecouteau.circle(t*36,85)
    tortuecouteau.end_fill()

    tortuecouteau.up()
    tortuecouteau.goto(j,k)
    tortuecouteau.down()

    #Petite touche de finition
    tortuecouteau.fillcolor('#9B937A')
    tortuecouteau.begin_fill()
    tortuecouteau.left(145)
    tortuecouteau.width(9*t)
    tortuecouteau.circle(t*120,8)
    tortuecouteau.right(108)
    tortuecouteau.forward(t*100)
    tortuecouteau.right(135)
    tortuecouteau.circle(t*36,30)
    tortuecouteau.right(75)
    tortuecouteau.width(2*t)
    tortuecouteau.forward(t*80)
    tortuecouteau.down()
    tortuecouteau.end_fill()

    tortuecouteau.width(2*t)
    tortuecouteau.up()
    tortuecouteau.forward(t*-30)
    tortuecouteau.left(90)
    tortuecouteau.forward(t*30)
    tortuecouteau.down()

    #Vis du couteau, pour maintenir la lame
    tortuecouteau.fillcolor('#A2A2A2')

    for i in range (3):
        tortuecouteau.begin_fill()  
        tortuecouteau.circle(t*10)
        tortuecouteau.end_fill()

        tortuecouteau.up()
        tortuecouteau.forward(t*70)
        tortuecouteau.down()

    #Détails sur la lame du couteau
    tortuecouteau.up()
    tortuecouteau.goto(e,r)
    tortuecouteau.down()
    tortuecouteau.right(90)
    tortuecouteau.forward(t*40)
    tortuecouteau.right(90)
    
    tortuecouteau.width(2*t)
    tortuecouteau.forward(t*220)
    tortuecouteau.circle(t*180,37)
    o,p=tortuecouteau.pos()
    tortuecouteau.right(30)
    tortuecouteau.circle(t*300,9)
    tortuecouteau.goto(o,p)
    tortuecouteau.left(160)
    tortuecouteau.circle(t*-180,34)

    
    update()
