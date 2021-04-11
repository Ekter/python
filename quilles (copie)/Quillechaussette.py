from setup import *
def chaussette(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)

    up()
    forward(t*-20)
    right(80)
    down()

    fillcolor('#ffca39')
    begin_fill()
    forward(t*50)
    circle(t*-18,90)
    circle(t*-70,20)
    circle(t*70,30)
    circle(t*30,160)
    circle(t*600,12)
    circle(t*30,90)
    forward(t*145)
    left(80)
    forward(t*70)
    left(96)
    forward(t*90)
    end_fill()

    up()
    left(5)
    forward(t*15)
    circle(t*-18,90)
    circle(t*-70,20)
    circle(t*70,30)
    fillcolor('#18850a')
    begin_fill()
    circle(t*30,160)
    jk,lm=pos()
    down()
    left(50)
    circle(t*35,110)
    end_fill()

    up()
    goto(jk,lm)
    right(160)
    down()
    right(2)
    circle(t*600,7)
    fillcolor('#c25253')
    begin_fill()
    circle(t*600,5)
    circle(t*30,90)
    az,fo=pos()
    forward(t*12)
    left(70)
    circle(t*60,93)
    end_fill()
    
    up()
    goto(az,fo)
    right(163)
    forward(t*100)
    down()

    begin_fill()
    for i in range(2):
        forward(t*20)
        left(85)
        forward(t*73)
        left(95)
    end_fill()
    

    update()



