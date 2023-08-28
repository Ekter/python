# Python - module turtle

Turtle est un module graphique simple pour Python. Il permet de dessiner des formes géométriques en utilisant des commandes simples. Il n'est pas approprié pour créer des applications graphiques complètes, mais il est parfait pour apprendre les bases de la programmation.

## Importer le module turtle

Pour utiliser le code d'un module externe, il faut utiliser l'instruction `import`. On peut choisir ce qu'on importe avec `from module import fonction`. Pour turtle, si on veut importer tout le module d'un coup, on peut utiliser la syntaxe suivante :

```py
from turtle import *
```

## Les fonctions de base

L'interface graphique de turtle est une fenêtre dans laquelle on peut déplacer un curseur. On peut ensuite utiliser des fonctions pour déplacer le curseur et dessiner des formes.

- `forward` : avance de la distance donnée
    ```py
    forward(100)
    ```
- `backward` : recule de la distance donnée
    ```py
    backward(100)
    ```
- `left` : tourne à gauche de l'angle donné
    ```py
    left(90)
    ```
- `right` : tourne à droite de l'angle donné
    ```py
    right(90)
    ```
- `goto` : va à la position donnée
    ```py
    goto(0, 0)
    ```
- `penup` : lève le stylo
    ```py
    penup()
    ```
- `pendown` : baisse le stylo
    ```py
    pendown()
    ```
- `pencolor` : change la couleur du stylo
    ```py
    pencolor("red")
    ```

## Exemple
Pour dessiner un carré, on peut utiliser le code suivant :

```py
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
```

Ou alors, avec les boucles :

```py
from turtle import *

for i in range(4):
    forward(100)
    left(90)
```


Exercices :
- Dessiner un triangle de 100 de coté
- Dessiner un pentagone
- Dessiner un hexagone
- Faire un programme qui dessine n'importe quel polygone régulier donné en input(nombre de faces)
- Dessiner un cercle

- Dessiner une étoile à 5 branches
- Dessiner une étoile dont le nombre de branches est donné en input

- dessiner un sapin de noël
