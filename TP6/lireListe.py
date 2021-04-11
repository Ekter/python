####################
# module lireListe #
####################

# Primitives pour lire des listes de mots, d'entiers et de flottants.
# Les listes sont données avec les éléments séparés par des espaces.
# exemple :
#     from lireListe import *
#     l = lireListeEntier("des entiers séparés par des espaces")
#     # l'utilisateur entre 5    -67  34 2
#     # l vaut [5, -67, 34, 2]

# lecture d'une liste de chaines de caractères
def lireListeMot(message):
    liste = input(message)
    listeChaine = liste.split()
    return listeChaine

# lecture d'une liste d'entiers
def lireListeEntier(message):
    liste = input(message)
    listeChaine = liste.split()
    resultat = []
    for nombre in listeChaine :
        resultat.append(int(nombre))
    return resultat


# lecture d'une liste de flottants
def lireListeFloat(message):
    liste = input(message)
    listeChaine = liste.split()
    resultat = []
    for nombre in listeChaine :
        resultat.append(float(nombre))
    return resultat