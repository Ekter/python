#Programme créé par Nino Mulac qui permet de dessiner des polygones, et par extension des cercles, des carrés, des triangles, et en bonus, des étoiles. Les paramètres sont le nombre de côtés et la longueur pour les polygones, seulement la longueur pour les carrés et triangles, et le rayon et la netteté pour les cercles. Pour les étoiles, l'unique parametre obligatoire est la longueur des côtés. Enfin, on peut pour toutes ces fonctions faire varier la position initiale et la couleur.

from turtle import *
#on va créer la procédure dessinpolygone

def dessinPolygone(nbCote,longueur,x=0,y=0,couleur="blue"):
    up()
    goto(x,y)
    down()
    pencolor(couleur)
    for k in range(nbCote):
        forward(longueur)
        left(360/nbCote)
#fin

#procédure cercle
def dessinCercle(rayon,precision,x=0,y=0,couleur="black"):
    up()
    goto(x,y)
    down()
    for k in range(precision):
        forward(rayon*2*3.1418/precision)
        left(360/precision)
#fin

#procédure triangle
def dessinTriangle(longueur,x=0,y=0,couleur="black"):
    dessinPolygone(3,longueur,x,y,couleur)
#procédure carré
def dessinCarre(longueur,x=0,y=0,couleur="black"):
    dessinPolygone(4,longueur,x,y,couleur)

#procédure étoile
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
dessinCercle(100,50,0,0,"blue")
speed(0)
circle(60) 
begin_fill()
dessinCarre(100)
end_fill()
dessinPolygone(7,100,100,-37,"blue")
dessinTriangle(100,53,153,"red")
fillcolor("yellow")
begin_fill()
dessinetoile5branches(200,-150,0,"blue")
end_fill()
input("")
