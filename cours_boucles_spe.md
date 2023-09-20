# Python - cas spéciaux sur les boucles


On a vu ensemble les boucles `for` et `while`. Il existe quelques cas spéciaux à connaître.

Rappel : `while` permet de répéter une action tant qu'une condition est vraie. `for` permet de répéter une action pour chaque élément d'une liste.

`while` est donc utile si on ne sait pas en avance combien de fois on va répéter l'action. `for` est utile si on sait combien de fois on va répéter l'action.

```py
a=5
while a > 0:
    print(a)
    a = a - 1

nouvelle_liste=range(5)
for i in nouvelle_liste:
    print(i)
```

## Boucles infinies

Il est possible de créer des boucles infinies, c'est-à-dire des boucles qui ne s'arrêtent jamais. On peut en faire uniquement avec les boucles `while`.

```py
while True:
    print("Je suis une boucle infinie")
# Je suis une boucle infinie
# Je suis une boucle infinie
# Je suis une boucle infinie
# Je suis une boucle infinie
# ...
```

## Boucles vides

Grâce à la condition de la boucle while, on peut créer des boucles qui ne font rien dans certains cas. Par exemple, si on veut afficher tous les nombres jusqu'à 0 à partir d'un nombre donné par l'utilisateur, on peut faire :

```py
a = int(input("Entrez un nombre : "))
while a > 0:
    print(a)
    a = a - 1
```

Dans ce cas, si le nombre donné par l'utilisateur est négatif, la boucle ne fait rien.


Exercice : 
* Faire un programme qui demande à l'utilisateur un nombre, et qui affiche tous les nombres pairs jusqu'à ce nombre.
* Faire un programme qui demande à l'utilisateur un nombre, et qui affiche tous les nombres premiers jusqu'à ce nombre.
* Combiner les boucles et l'ouverture de fichier pour afficher le contenu d'un fichier ligne par ligne, en s'arretant à la première ligne vide. Rappel : on peut utiliser break pour arreter la boucle
* 
Exemple de fichier :
```
Bonjour,
Je suis un fichier texte de trois lignes.
La constante de Plik est 37 très exactement.

```

Autre fichier sur lequel ça doit marcher :
```
Bonjour,

```

Et :
```
1
2
3
4
5
6
7
8
9
10

```
Dans ce cas on est obligés d'utiliser while car on ne sait pas à l'avance combien de lignes il y a dans le fichier.
