# Python - Tkinter

Tkinter est une librairie graphique pour Python. Elle permet de créer des interfaces graphiques.

Cette librairie est installée par défaut avec Python.

Elle n'est pas très puissante et ne permet pas de créer des interfaces très élaborées, mais elle est simple à utiliser et permet de créer rapidement des interfaces graphiques.

## Créer une fenêtre

Le code minimal pour créer une fenêtre est le suivant :

```python
from tkinter import *

fenetre = Tk() # Création de la fenêtre

fenetre.mainloop() # Boucle infinie qui permet d'afficher la fenêtre
```

## Ajouter des widgets

Les widgets sont les éléments graphiques de l'interface : boutons, zones de texte(label ), etc.

On peut les créer avec leurs options de configuration en une seule ligne :

```python
from tkinter import *

fenetre = Tk()

bouton = Button(fenetre, text="Mon bouton", bg="red", fg="white")

bouton.pack() # Affichage du bouton

label = Label(fenetre, text="Mon texte")

label.pack() # Affichage du label

fenetre.mainloop()
```

## Affichage

Il existe plusieurs méthodes pour afficher les widgets dans la fenêtre.

La plus simple est d'utiliser la méthode `pack()`, qui rajoute juste notre élément en dessous des autres.

On peut aussi utiliser la méthode `grid()` qui permet de placer les éléments dans une grille:

```python
from tkinter import *

fenetre = Tk()

bouton1 = Button(fenetre, text="Mon bouton 1", bg="red", fg="white")
bouton2 = Button(fenetre, text="Mon bouton 2", bg="green", fg="white")
bouton3 = Button(fenetre, text="Mon bouton 3", bg="blue", fg="white")
label = Label(fenetre, text="Mon texte qui est grand bonc il va décaler la grille")

bouton1.grid(row=0, column=0) # Affichage du bouton 1 en haut à gauche
bouton2.grid(row=0, column=1) # Affichage du bouton 2 à droite du bouton 1
bouton3.grid(row=1, column=0) # Affichage du bouton 3 en dessous du bouton 1
label.grid(row=1, column=1) # Affichage du label à droite du bouton 3

fenetre.mainloop()
```

## Gestion des événements

On peut faire en sorte que des fonctions soient appelées lorsqu'un événement se produit sur un widget.

Par exemple, on peut vouloir changer un texte lorsqu'on clique sur un bouton.

Pour cela, on peut utiliser la méthode `bind()` qui permet d'associer une fonction à un événement.

```python
from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Mon texte")
bouton = Button(fenetre, text="Mon bouton")

def change_texte(event):
    label.config(text="Mon nouveau texte")

bouton.bind("<Button-1>", change_texte) # Lorsqu'on clique sur le bouton gauche de la souris, on appelle la fonction change_texte

label.pack()
bouton.pack()

fenetre.mainloop()
```

## Exercices

1. Faire une interface avec une zone de texte et 4 boutons. Chaque bouton a un numéro. Cliquer sur un bouton remplace le texte par le numéro du bouton.
2. Faire une interface qui liste les fichiers d'un dossier (rappel : import os, os.listdir("dossier")). Chaque fichier doit apparaitre dans une zone de texte différente. Dans l'idéal, il faudrait utiliser une boucle pour que ça marche peu importe le dossier et le nombre de fichiers.



## Notions à voir avant de pouvoir faire des interfaces graphiques complètes:

1. La programmation orientée objet. C'est l'extension des fonctions pour être encore plus généraliste. Ça permet de créer des widgets personnalisés entre autres.
2. Les modules.
   1. On peut séparer du code en plusieurs fichiers pour s'y retrouver plus facilement(librairies)
   2. On peut ajouter des librairies externes pour ajouter des fonctionnalités à Python.
3. Les exceptions. C'est un moyen de gérer les erreurs de façon à ce que l'interface ne plante pas si l'utilisateur fait n'importe quoi.

Autres notions importantes mais pas nécessaires :
1. Les décorateurs. C'est un moyen de modifier le comportement d'une fonction sans la modifier.
2. La programmation sur plusieurs threads. C'est un moyen de faire plusieurs choses en même temps. Ça permet par exemple de faire une interface graphique qui ne se bloque pas lorsqu'on fait une opération longue.
3. La programmation asynchrone. C'est un autre moyen de faire plusieurs choses en même temps. Ça permet par exemple de faire une interface graphique qui fait autre chose pendant qu'on attend une réponse d'un serveur.
4. Les générateurs. C'est un moyen de créer des objets qui génèrent des valeurs au fur et à mesure qu'on les demande. Ça permet par exemple de faire une interface graphique qui affiche des valeurs au fur et à mesure qu'on les reçoit d'un serveur.
5. Les expressions régulières. C'est un moyen de faire des recherches dans du texte. Ça permet par exemple de faire une interface graphique qui recherche des mots dans un texte.
