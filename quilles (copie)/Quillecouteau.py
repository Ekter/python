from setup import *
def couteau(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)

    width(7*t)
    pencolor('black')

    #Lame du couteau
    fillcolor('grey')
    begin_fill()
    left(41)
    for i in range (6):
        
        width(7*t)
        forward(t*21)
        a,z=pos()
        right(90)
        width(5*t)
        forward(t*20)
        left(90)
        goto(a,z)
        
    width(7*t)
    forward(t*160)
    right(10)
    forward(t*137)
    right(110)
    circle(t*-180,60)
    forward(t*225)
    width(9*t)
    left(45)
    forward(t*10)
    right(45)
    e,r=pos()
    width(8*t)
    forward(t*23)
    right(90)
    forward(t*25)
    left(90)
    forward(t*15)
    right(90)
    width(15*t)
    forward(t*150)
    end_fill()

    #Haut du manche
    fillcolor('#3E3E3C')
    begin_fill()
    width(9*t)
    left(90)
    forward(t*30)
    left(90)
    forward(t*190)
    left(90)
    forward(t*30)
    left(90)
    forward(t*35)

    end_fill()

    up()
    forward(t*5)
    left(90)
    forward(t*35)
    down()

    right(40)
    circle(t*36,90)
    right(100)
    circle(t*36,95)
    right(100)
    circle(t*36,95)
    right(80)
    circle(t*36,90)

    #Bas du manche
    fillcolor('#9B937A')
    begin_fill()
    circle(t*36,30)
    circle(t*-6,180)
    left(40)

    circle(t*-110,60)
    right(55)
    circle(t*-50,30)
    width(2*t)
    right(90)
    circle(t*140,40)
    end_fill()

    #Manche
    fillcolor('#34322A')
    begin_fill()
    left(180)
    circle(t*-140,40)
    width(9*t)
    right(80)
    circle(t*100,30)
    circle(t*-150,30)
    circle(t*120,30)
    j,k=pos()
    right(105)
    width(8*t)
    forward(t*90)
    right(110)
    circle(t*36,70)
    right(100)
    circle(t*36,95)
    right(100)
    circle(t*36,95)
    right(80)
    circle(t*36,85)
    end_fill()

    up()
    goto(j,k)
    down()

    #Petite touche de finition
    fillcolor('#9B937A')
    begin_fill()
    left(145)
    width(9*t)
    circle(t*120,8)
    right(108)
    forward(t*100)
    right(135)
    circle(t*36,30)
    right(75)
    width(2*t)
    forward(t*80)
    down()
    end_fill()

    width(2*t)
    up()
    forward(t*-30)
    left(90)
    forward(t*30)
    down()

    #Vis du couteau, pour maintenir la lame
    fillcolor('#A2A2A2')

    for i in range (3):
        begin_fill()  
        circle(t*10)
        end_fill()

        up()
        forward(t*70)
        down()

    #Détails sur la lame du couteau
    up()
    goto(e,r)
    down()
    right(90)
    forward(t*40)
    right(90)
    
    width(2*t)
    forward(t*220)
    circle(t*180,37)
    o,p=pos()
    right(30)
    circle(t*300,9)
    goto(o,p)
    left(160)
    circle(t*-180,34)

    
    update()

