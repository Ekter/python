# Feuille de calcul sur tkinter

Je vais essayer de te guider pour faire la feuille de calcul.

Voici la structure du code que j'ai fait:

```py
from tkinter import *

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Feuille de calcul")

class Feuille:
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.label = Label(self.frame, text="Feuille de calcul")
        self.label.grid(row=0, column=0, columnspan=2)

        self.champ_de_texte = 0 #à compléter (on peut réutiliser un ChampDeTexte
        # fait la dernière fois, sinon il faut mettre un label puis une Entry et
        # un bouton pour valider)
        # Il faut aussi faire le bind pour appeler la méthode calculer quand on
        # appuie sur entrée ou clique sur le bouton

        self.label_resultats = Label(self.frame, text="Résultats")
        self.label_resultats.grid(row=3, column=0, columnspan=2)
        self.resultats = Resultats(self.frame)

    def afficher(self):
        self.frame.pack()

    def calculer(self):
        # à compléter (il faut appeler la méthode nombre_premiers et faire une
        # boucle pour ajouter les résultats à la frame)
        self.resultats.ajouter_resultat("Résultat à remplacer par le calcul de nombre_premiers")


class Resultats:
    def __init__(self, parent):
        self.frame = Frame(parent)


    def ajouter_resultat(self, texte):
        # à compléter (il faut créer un label et l'ajouter à la frame, on peut
        # utiliser la méthode pack pour que ce soit plus simple)
        print("Résultat à remplacer par le calcul de nombre_premiers")


feuille = Feuille(fenetre)

feuille.afficher()

fenetre.mainloop()
```

Le mot clé `pass` signifie qu'on ne fait rien. Il permet de faire des fonctions
qui ne font rien, je l'ai mis un peu partout pour que tu puisses éxécuter le
code avant d'avoir tout remplis.

La démarche la mieux à suivre est probablement de commencer par remplir la
classe résultat, puis la classe feuille, puis la méthode calculer.

## Import

Si tu veux réutiliser des fonctions ou des classes d'un autre programme, il faut
utiliser `import`, comme `from turtle import *` ou `from tkinter import *`.

Exemple pour importer toutes les fonctions de Brouillon.py( pas besoin du .py
dans le import):

```py
from Brouillon import *

#on peut maintenant utiliser les fonctions de Brouillon.py
```

Exemple pour importer seulement la fonction `nombre_premiers` de Brouillon.py:

```py
from Brouillon import nombre_premiers
```

On peut aussi importer un module par son nom, c'est pratique dans les cas où
plusieurs modules ont des fonctions qui ont le même nom:

```py

import Brouillon

#on peut maintenant utiliser les fonctions de Brouillon.py en faisant
Brouillon.fonction()
```
