#programme créé par Nino Mulac qui utilise la fonction dessine polygone de turtlepolygone(créé par moi aussi) pour dessiner une liste de polygones. Comme la moitié des arguments sont optionnels, je fais différents cas.
from turtlepolygone import *
def listepolygones(liste):
    for sousliste in liste:
        if len(sousliste)==2:
            dessinPolygone(sousliste[0],sousliste[1])
        if len(sousliste)==4:
            dessinPolygone(sousliste[0],sousliste[1],sousliste[2],sousliste[3])
        if len(sousliste)==5:
            dessinPolygone(sousliste[0],sousliste[1],sousliste[2],sousliste[3],sousliste[4])
#fin

listepolygones([[3,150],[6,50,-100,-100],[8,50,100,100,"red"]])
input("")
