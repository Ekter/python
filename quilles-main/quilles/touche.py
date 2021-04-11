from turtle import*

def touche(tortue,longueur,largeur,épaisseur,texte="6",taille=20,ajustement=0):
    tortue.pencolor('black')
    tortue.begin_fill()

    for i in range(2):
            tortue.forward(longueur)
            tortue.tortue.left(45)
            tortue.forward(épaisseur)
            tortue.left(45)
            tortue.forward(largeur)
            tortue.left(45)
            tortue.forward(épaisseur)
            tortue.left(45)

    tortue.end_fill()
    (x,y)=tortue.pos()
    tortue.up()
    tortue.forward((longueur-len(texte)*(12/20)*taille)/2)
    tortue.left(90)
    tortue.forward((largeur/1.25-taille)/1.5)
    tortue.forward(ajustement)
    tortue.right(90)
    tortue.down()
    tortue.pencolor('white')
    tortue.write(texte, font=("Arial", int(taille), "normal"))
    
    tortue.up()
    tortue.goto(x,y)
    tortue.down()
