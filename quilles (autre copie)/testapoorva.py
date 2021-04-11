from turtle import *

def chifletre(taille,bi):

    #composition=[s,se,ne,n,no,m,so])

    binaire=bi
    
    t=taille
    tracer(0)
    width(5*t)
    
    if binaire[0]=="0":
        up()
    forward(10*t)
    down()
    
    left(90)
    if binaire[1]=="0":
        up()
    forward(10*t)
    down()
    
    if binaire[2]=="0":
        up()
    forward(10*t)
    down()
    left(90)
    
    if binaire[3]=="0":
        up()
    forward(10*t)
    down()
    
    left(90)
    if binaire[4]=="0":
        up()
    forward(10*t)
    down()
    
    left(90)
    if binaire[5]=="0":
        up()
    forward(10*t)
    backward(10*t)
    right(90)
    down()

    if binaire[6]=="0":
        up()
    forward(10*t)
    
    
    update()

chifletre(1,"10110110")
input("")
    