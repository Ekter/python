from setup import *

def cafe(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)
    
    width(5*t)

    up()
    backward(t*194)
    left(90)
    forward(t*43)
    right(90)
    down()

    #Le bol de la tasse
    fillcolor('#e43f39')
    begin_fill()
    forward(t*322)
    right(77)
    circle(t*-200,60)
    right(2)
    circle(t*-70,50)
    left(10)
    forward(t*85)
    left(10)
    circle(t*-70,50)
    right(2)
    circle(t*-200,62)
    end_fill()
    
    
    left(180)
    circle(t*200,5)
    right(180)

    #Le rebord de la tasse
    fillcolor('#f8c9cf')
    begin_fill()
    circle(t*200,5)
    right(87)
    forward(t*322)
    right(77)
    circle(t*200,5)
    up()
    right(108)
    forward(t*324)
    end_fill()
    
    up()
    backward(t*324)
    left(108)
    circle(t*200,2)
    left(110)
    down()

    #L'anse de la tasse
    fillcolor('#e43f39')
    begin_fill()
    circle(t*-30,60)
    circle(t*-70,50)
    circle(t*-40,60)
    left(20)
    circle(t*-100,74.5)
    right(122)
    circle(t*200,8.5)
    right(50)
    circle(t*80,70)
    circle(t*30,120)
    right(110)
    circle(t*200,5)
    end_fill()

    left(180)
    circle(t*-200,52)
    right(2)
    circle(t*-70,40)

    #Le pied de la tasse
    
    begin_fill()
    left(5)
    circle(t*-500,14)
    left(90)
    forward(t*12)
    left(95)
    forward(t*125)
    left(110)
    forward(t*12)
    end_fill()

    up()
    backward(t*-20)
    left(90)
    forward(t*158)
    left(71)
    down()

    #Le pied de la coupole
    

    fillcolor('#376d72')
    begin_fill()
    forward(t*15)
    left(90)
    forward(t*215)
    left(90)
    forward(t*15)
    left(90)
    forward(t*215)
    end_fill()

    #La coupole

    fillcolor('#66c4d6')
    begin_fill()
    forward(t*60)
    right(45)
    forward(t*30)
    right(135)
    forward(t*370)
    right(135)
    forward(t*30)
    right(45)
    forward(t*300)
    end_fill()

    up()
    backward(t*120)
    right(90)
    forward(t*270)
    down()

    #La fumée qui s'échappe du café

    right(60)
    circle(t*37,120)
    left(8)
    circle(t*-80,25)
    circle(t*-40,240)
    circle(t*-17,200)
    

    

    update()


