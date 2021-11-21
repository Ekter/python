#on va créer la procédure dessinpolygone
from turtle import *
def dessinpolygone(nbCote,longueur,x=0,y=0,couleur="black"):
    up()
    goto(x,y)
    down()
    pencolor(couleur)
    for k in range(nbCote):
        forward(longueur)
        left(360/nbCote)
#fin

#et en bonus: une étoile
def dessinetoile5branches(longueur,x=0,y=0,couleur="yellow"):
    up()
    goto(x,y)
    down()
    pencolor(couleur)
    left(18)
    for i in range(5):
        forward(longueur)
        left(72)
        forward(longueur)
        right(144)
    right(18)
#fin

#sapin:(il y a 15 triangles verts par pointe, et j'en ai fait 4)
speed(0)
dessinpolygone(4,50,25,-100,"brown")
for k in range(1,5):
    for i in range(15):
        dessinpolygone(3,(100-15*k)/1.1**i,50-(100-15*k)/1.1**i/2,-50+i+50*(k-1)-5*k,"green")
dessinetoile5branches(15,30,130)
input("")
