# Python - Programmation orientée objet pour les interfaces graphiques

La programmation orientée objet est un paradigme de programmation qui permet de structurer son code en classes, des especes de conteneurs qui contiennent des variables et des fonctions.

C'est un paradigme très utilisé en Python, et notamment pour les interfaces graphiques.

Par exemple, on peut créer une classe `Voiture` qui contient des variables comme `couleur` ou `vitesse` et des fonctions comme `accelerer()` ou `freiner()`.
On peut ensuite créer des objets de cette classe, comme `ma_voiture_rouge = Voiture(couleur="rouge")`.

Par convention, les noms de classes commencent par une majuscule pour les distinguer des fonctions.

## Création d'une classe:

Exemple de définition d'une classe:

```python

class Voiture:
    def __init__(self, couleur):
        self.couleur = couleur
        self.vitesse = 0

    def accelerer(self):
        self.vitesse += 10

    def freiner(self):
        self.vitesse -= 10
```

Voici notre conteneur `Voiture`.

Le mot-clef self représente l'objet lui-même. On peut noter qu'il est présent en premier paramètre de toutes les fonctions de la classe.

On peut voir qu'il a deux variables (on les appelle des attributs) `couleur` et `vitesse`, et deux fonctions (on les appelle des méthodes) `accelerer()` et `freiner()`.

La méthode `__init__()` est spéciale : c'est la méthode qui est appelée quand on crée un objet de la classe. Elle permet d'initialiser les attributs de l'objet.

Pour créer des objets (des instances de la classe), on utilise :

```python
ma_voiture_rouge = Voiture(couleur="rouge")
ma_voiture_bleue = Voiture(couleur="bleue")

```

Pour récupérer les attributs d'un objet, on utilise le point :

```python
print(ma_voiture_rouge.couleur) # rouge
print(ma_voiture_rouge.vitesse) # 0
```

Pour appeler une méthode d'un objet, on utilise le point et les parenthèses, comme une fonction normale :

```python
ma_voiture_rouge.accelerer()
print(ma_voiture_rouge.vitesse) # 10
```

## Utilisation pour les interfaces graphiques

On peut utiliser les classes pour créer des ensembles de widgets qui doivent être affichés ensemble par exemple.

Imaginons qu'on veuille faire un label qui dit "Nom:", une zone de texte dans lequel l'utilisateur doit mettre son nom, et un bouton pour valider. On peut faire un classe ChampDeTexte qui contient ces trois widgets.

L'avantage principal est qu'on peut réutitiliser cette classe pour différents cas, par exemple pour récupérer aussi le prénom, ou un mot de passe.

```python
from tkinter import *

class ChampDeTexte:
    def __init__(self, fenetre, texte):
        self.label = Label(fenetre, text=texte)
        self.entrée = Entry(fenetre)
        self.bouton = Button(fenetre, text="Valider")

    def afficher(self):
        self.label.pack()
        self.entrée.pack()
        self.bouton.pack()

fenetre = Tk()

champ1 = ChampDeTexte(fenetre, "Nom :")
champ1.afficher()

champ2 = ChampDeTexte(fenetre, "Prénom :")
champ2.afficher()

fenetre.mainloop()
```

## Les frames sur Tkinter

Les frames sont des zones de l'interface qui permettent de regrouper des widgets.

Elles sont pratiques pour structurer son interface, puisqu'on peut gérer la disposition des widgets dans une frame, et ensuite disposer les frames dans la fenêtre.

C'est en général une bonne idée de créer une frame qui regroupe les widgets de chaque objet qu'on crée, pour les gérer plus facilement.

```python
from tkinter import *

class ChampDeTexte:
    def __init__(self, fenetre, texte):
        self.frame = Frame(fenetre, bg="grey")
        self.label = Label(self.frame, text=texte)
        self.entrée = Entry(self.frame)
        self.bouton = Button(self.frame, text="Valider")

    def afficher(self):
        self.frame.pack()
        self.label.pack()
        self.entrée.pack()
        self.bouton.pack()

fenetre = Tk()

champ1 = ChampDeTexte(fenetre, "Nom :")
champ1.afficher()

champ2 = ChampDeTexte(fenetre, "Prénom :")
champ2.afficher()

fenetre.mainloop()
```

## Exercice

Créer une classe DoubleBouton qui contient deux boutons et un label, et qui affiche un message différent quand on clique sur chaque bouton.
Les boutons doivent être l'un en dessous de l'autre, et le label doit être à côté des boutons.

En récupérant le code de ChampDeTexte, créer une classe PleinDeChampsDeTextes dont le constructeur prend en paramètre une liste de textes, et qui crée un ChampDeTexte pour chaque texte de la liste.


Puis faire une interface avec plusieurs objets de ces deux classes.

## Héritage

L'héritage permet de créer une classe qui hérite des attributs et des méthodes d'une autre classe.
C'est l'avantage principal des classes, dans le cas où on veut créer plusieurs objets qui ont des attributs et des méthodes en commun.

Par exemple, on peut créer une classe `Véhicule` qui contient des variables comme `vitesse` et `nombre_de_places` et des fonctions comme `freiner()`.
On peut ensuite créer une voiture, qui hériterait de la classe `Véhicule`, et qui aurait en plus une variable `couleur` et une fonction `accelerer()`.
Et on pourrait créer un vélo, qui hériterait aussi de la classe `Véhicule`, et qui aurait en plus une variable `taille` et une fonction `tourner()`.

```python

class Véhicule:
    def __init__(self):
        self.vitesse = 0
        self.nombre_de_places = 0

    def freiner(self):
        print("Ça va trop vite !")

class Voiture(Véhicule):
    def __init__(self):
        super().__init__()
        self.couleur = "rouge"

    def accelerer(self):
        self.vitesse += 10

class Vélo(Véhicule):
    def __init__(self):
        super().__init__()
        self.taille = 28

    def tourner(self):
        print("Je tourne !")
```

On peut utiliser la fonction `super()` pour appeler les méthodes de la classe parente. Il est important d'appeler la méthode `__init__()` de la classe parente pour initialiser les attributs de la classe parente.

On peut ensuite créer des objets de ces classes :

```python
ma_voiture = Voiture()
mon_vélo = Vélo()
```

La méthode isInstance() permet de savoir si un objet est une instance d'une classe :

```python

print(isinstance(ma_voiture, Voiture)) # True
print(isinstance(ma_voiture, Véhicule)) # True
print(isinstance(ma_voiture, Vélo)) # False
```


En utilisant cette méthode, on peut créer des classes qui héritent d'objets graphiques, et qui peuvent être utilisées comme des objets graphiques.

Ça permet de rajouter toutes les méthodes dont on a besoin qu'on estime manquantes dans les objets graphiques.
