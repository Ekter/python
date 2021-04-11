from turtle import*

def touche(tortue,longueur,largeur,épaisseur,texte="6",taille=20,ajustement=0):
    tortue.pencolor('black')

    for i in range(2):
            tortue.forward(longueur)
            tortue.left(45)
            tortue.forward(épaisseur)
            tortue.left(45)
            tortue.forward(largeur)
            tortue.left(45)
            tortue.forward(épaisseur)
            tortue.left(45)

