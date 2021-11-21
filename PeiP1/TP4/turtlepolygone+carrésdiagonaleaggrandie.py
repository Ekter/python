#Programme créé par Nino Mulac qui permet de dessiner des polygones, et par extension des cercles, des carrés, des triangles, et en bonus, des étoiles. Les paramètres sont le nombre de côtés et la longueur pour les polygones, seulement la longueur pour les carrés et triangles, et le rayon et la netteté pour les cercles. Pour les étoiles, l'unique parametre obligatoire est la longueur des côtés. Enfin, on peut pour toutes ces fonctions faire varier la position initiale et la couleur.
#Et là j'ai rajouté les carrés en diagonale

from turtle import *

#on va créer la procédure dessinpolygone
def dessinPolygone(nbCote,longueur,x=0,y=0,couleur="black"):
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

#procedure pour les carrés en diagonale qui grandissent: je calcule la position avec la somme d'une suite géométrique de premier terme longueur et de ratio facteur.
def dessincarresaggrandis(longueur,nombre,facteur):
    for i in range(1,nombre+1):
        dessinCarre(longueur*facteur**i,longueur*(1-facteur**i)/(1-facteur),longueur*(1-facteur**i)/(1-facteur))
#fin

speed(0)
dessincarresaggrandis(10,5,2)

input("")