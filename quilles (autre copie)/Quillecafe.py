from setup import *

def cafe(taille,x,y,angle=0):

    tortuecafe=Turtle(undobuffersize=0,visible=False,shape="square")
    setup(x,y,angle,tortuecafe)

    t=taille/8

    tracer(0)
    
    tortuecafe.width(5*t)

    tortuecafe.up()
    tortuecafe.backward(t*194)
    tortuecafe.left(90)
    tortuecafe.forward(t*43)
    tortuecafe.right(90)
    tortuecafe.down()

    #Le bol de la tasse
    tortuecafe.fillcolor('#e43f39')
    tortuecafe.begin_fill()
    tortuecafe.forward(t*322)
    tortuecafe.right(77)
    tortuecafe.circle(t*-200,60)
    tortuecafe.right(2)
    tortuecafe.circle(t*-70,50)
    tortuecafe.left(10)
    tortuecafe.forward(t*85)
    tortuecafe.left(10)
    tortuecafe.circle(t*-70,50)
    tortuecafe.right(2)
    tortuecafe.circle(t*-200,62)
    tortuecafe.end_fill()
    
    
    tortuecafe.left(180)
    tortuecafe.circle(t*200,5)
    tortuecafe.right(180)

    #Le rebord de la tasse
    tortuecafe.fillcolor('#f8c9cf')
    tortuecafe.begin_fill()
    tortuecafe.circle(t*200,5)
    tortuecafe.right(87)
    tortuecafe.forward(t*322)
    tortuecafe.right(77)
    tortuecafe.circle(t*200,5)
    tortuecafe.up()
    tortuecafe.right(108)
    tortuecafe.forward(t*324)
    tortuecafe.end_fill()
    
    tortuecafe.up()
    tortuecafe.backward(t*324)
    tortuecafe.left(108)
    tortuecafe.circle(t*200,2)
    tortuecafe.left(110)
    tortuecafe.down()

    #L'anse de la tasse
    tortuecafe.fillcolor('#e43f39')
    tortuecafe.begin_fill()
    tortuecafe.circle(t*-30,60)
    tortuecafe.circle(t*-70,50)
    tortuecafe.circle(t*-40,60)
    tortuecafe.left(20)
    tortuecafe.circle(t*-100,74.5)
    tortuecafe.right(122)
    tortuecafe.circle(t*200,8.5)
    tortuecafe.right(50)
    tortuecafe.circle(t*80,70)
    tortuecafe.circle(t*30,120)
    tortuecafe.right(110)
    tortuecafe.circle(t*200,5)
    tortuecafe.end_fill()

    tortuecafe.left(180)
    tortuecafe.circle(t*-200,52)
    tortuecafe.right(2)
    tortuecafe.circle(t*-70,40)

    #Le pied de la tasse
    
    tortuecafe.begin_fill()
    tortuecafe.left(5)
    tortuecafe.circle(t*-500,14)
    tortuecafe.left(90)
    tortuecafe.forward(t*12)
    tortuecafe.left(95)
    tortuecafe.forward(t*125)
    tortuecafe.left(110)
    tortuecafe.forward(t*12)
    tortuecafe.end_fill()

    tortuecafe.up()
    tortuecafe.backward(t*-20)
    tortuecafe.left(90)
    tortuecafe.forward(t*158)
    tortuecafe.left(71)
    tortuecafe.down()

    #Le pied de la coupole
    

    tortuecafe.fillcolor('#376d72')
    tortuecafe.begin_fill()
    tortuecafe.forward(t*15)
    tortuecafe.left(90)
    tortuecafe.forward(t*215)
    tortuecafe.left(90)
    tortuecafe.forward(t*15)
    tortuecafe.left(90)
    tortuecafe.forward(t*215)
    tortuecafe.end_fill()

    #La coupole

    tortuecafe.fillcolor('#66c4d6')
    tortuecafe.begin_fill()
    tortuecafe.forward(t*60)
    tortuecafe.right(45)
    tortuecafe.forward(t*30)
    tortuecafe.right(135)
    tortuecafe.forward(t*370)
    tortuecafe.right(135)
    tortuecafe.forward(t*30)
    tortuecafe.right(45)
    tortuecafe.forward(t*300)
    tortuecafe.end_fill()

    tortuecafe.up()
    tortuecafe.backward(t*120)
    tortuecafe.right(90)
    tortuecafe.forward(t*270)
    tortuecafe.down()

    #La fumée qui s'échappe du café

    tortuecafe.right(60)
    tortuecafe.circle(t*37,120)
    tortuecafe.left(8)
    tortuecafe.circle(t*-80,25)
    tortuecafe.circle(t*-40,240)
    tortuecafe.circle(t*-17,200)

    update()
