from turtle import *

def carré (x,y,couleur="black"):
    up()
    goto (x,y)
    
    down()
    co=pencolor(couleur)
   
    i =0
    while i<4:
        forward(5)
        left(90)
        i+=1

carré(200,20)
screen.update()
 
