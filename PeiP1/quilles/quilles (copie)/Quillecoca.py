from setup import *
def coca(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)

    up()
    forward(t*54)

    left(90)
    forward(t*14)
    down()
    right(90)

    #Bouteille en verre
    fillcolor('#9fccf6')
    pencolor('#9fccf6')
    begin_fill()
    forward(t*6)
    right(100)
    circle(t*-300,8)
    circle(t*140,40)
    right(3)
    circle(t*-300,10)
    right(5)
    circle(t*-500,5.9)
    circle(t*-20,78)
    left(6)
    circle(t*-230,34)
    circle(t*-20,78)
    right(2.5)
    circle(t*500,5.9)
    right(5)
    circle(t*-300,10)
    right(5)
    circle(t*140,40)
    right(2)
    circle(t*-300,7)
    right(101)
    left(110)
    circle(t*-100,37)
    left(5)
    circle(t*-200,20)
    left(5)
    circle(t*150,31)
    right(91)
    forward(t*55)
    right(91)
    circle(t*150,31)
    left(0)
    circle(t*-200,20)
    left(3)
    circle(t*-100,37)
    end_fill()

    #Coca en liquide
    width(1*t)
    left(13)
    up()
    left(90)
    forward(t*-5)
    right(90)
    down()
    pencolor('#030b1a')
    fillcolor('#030b1a')
    begin_fill()
    circle(t*-300,10)
    circle(t*100,40)
    circle(t*-300,10)
    right(5)
    circle(t*-500,5.9)
    circle(t*-20,78)
    left(3)
    circle(t*-200,32)
    circle(t*-20,78)
    right(3)
    circle(t*500,5.9)
    right(5)
    circle(t*-300,10)
    circle(t*100,40)
    right(2)
    circle(t*-300,9)
    circle(t*-100,43)
    right(57)
    forward(t*113)
    right(63)
    circle(t*-100,43)
    end_fill()

    up()
    left(177)
    right(94)
    forward(t*11.5)
    left(94)
    
    #Etiquette rouge 
    fillcolor('#ab0000')
    begin_fill()
    circle(t*100,37)
    left(71)
    forward(t*150)
    left(71)
    circle(t*100,37)
    left(73)
    forward(t*150)
    end_fill()


    up()
    backward(t*40)
    left(90)
    forward(t*10)
    down()

    #Etiquette avec l'inscription coca
    fillcolor('#cdd0d5')
    begin_fill()
    right(90)
    circle(t*15,180)
    forward(t*85)
    circle(t*15,180)
    forward(t*85)
    end_fill()

    up()
    backward(t*85)
    down()
    write('COCA', font=("Arial", int(t*20), "normal"))
    
    up()
    forward(t*10)
    right(90)
    forward(t*30)
    down()

    #Bulle de coca
    pencolor('#cdd0d5')
    dot(t*10)

    up()
    forward(t*10)
    right(90)
    forward(t*-30)
    down()

    dot(t*25)

    up()
    forward(t*10)
    right(90)
    forward(t*-30)
    down()

    dot(t*10)

    up()
    right(90)
    forward(t*30)
    down()

    dot(t*15)

    up()
    left(50)
    forward(t*30)
    down()

    dot(t*12)

    up()
    left(39)
    pencolor('#ab0000')
    forward(t*240)
    down()

    #Bouchon rouge
    fillcolor('#ab0000')
    begin_fill()
    right(80)
    circle(t*15,170)
    forward(t*45)
    circle(t*15,180)
    forward(t*50)
    end_fill()

    
    
    update()

