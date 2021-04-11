from turtle import*

def touche(longueur,largeur,épaisseur,texte="6",taille=20,ajustement=0):
    pencolor('black')
    begin_fill()

    for i in range(2):
            forward(longueur)
            left(45)
            forward(épaisseur)
            left(45)
            forward(largeur)
            left(45)
            forward(épaisseur)
            left(45)

    end_fill()
    (x,y)=pos()
    up()
    forward((longueur-len(texte)*(12/20)*taille)/2)
    left(90)
    forward((largeur/1.25-taille)/1.5)
    forward(ajustement)
    right(90)
    down()
    pencolor('white')
    write(texte, font=("Arial", int(taille), "normal"))
    
    up()
    goto(x,y)
    down()
