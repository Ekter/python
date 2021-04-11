#programme de Nino Mulac qui donne la moyenne en fonction de notes et de coeffs.

from lireListe import *
continuer="o"
while continuer!="n":
    listenotes=lireListeEntier("Notes: ")
    listecoeff=lireListeEntier("Coeffs: ")
    somme=0
    for k in range(len(listenotes)):
        somme+=listenotes[k]*listecoeff[k]
    print(somme,sum(listecoeff),somme/(sum(listecoeff)))
    continuer=input("Continuer? ")
