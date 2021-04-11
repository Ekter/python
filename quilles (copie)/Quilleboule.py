from setup import *
def boule(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)

    #La boule noire
    up()
    right(90)
    backward(t*150)
    right(90)
    
    begin_fill()
    circle(t*200,360)
    end_fill()

    #Le cercle blanc
    left(90)
    pencolor('blue')
    forward(t*130)
    right(90)

    fillcolor('white')
    begin_fill()
    circle(t*75,360)
    end_fill()

    #Ecriture du 8

    left(90)
    forward(t*145)
    right(90)
    forward(t*30)

    write('8', font=("Arial",int(90*t), "normal"))

    update()

