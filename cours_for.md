# Listes et boucles `for` en python

Les listes en python sont des ensembles de valeurs. Elles n'ont pas une taille fixe et peuvent contenir des valeurs de différents types. On les définit avec la syntaxe suivante :

```py
nom_de_la_liste = [valeur_1, valeur_2, valeur_3, ...]
```

On peut accéder à une valeur de la liste avec la syntaxe suivante :

```py
nom_de_la_liste[index]
```
Mais atttention! Les index commencent à 0, donc la première valeur de la liste est à l'index 0, la deuxième à l'index 1, etc.

Example :

```py
liste = [1, 2, 3, '4']
print(liste)
liste[3] = int(liste[3])
print(liste)
```

## Fonctions utiles pour les listes

- `len` : renvoie la taille de la liste
    ```py
    liste = [1, 2, 3]
    len(liste) # 3
    ```
- `append` : ajoute une valeur à la fin de la liste
    ```py
    liste = [1, 2, 3]
    liste.append(4)
    print(liste) # [1, 2, 3, 4]
    ```
- `remove` : supprime la première occurence de la valeur donnée
    ```py
    liste = [1, 2, 3, 2]
    liste.remove(2)
    print(liste) # [1, 3, 2]
    ```
- `index` : renvoie l'index de la première occurence de la valeur donnée
    ```py
    liste = [1, 2, 3, 2]
    liste.index(2) # 1
    ```


## Boucles `for`

Les boucles les plus simples en Python sont les boucles `for`. Ce sont de boucles qui vont répeter une action tant que leur liste n'est pas terminée.

Exemple :
```py
liste = [1, 2, 3, '4', 5.0]
for element in liste:
    print(element, type(element))
```

On peut utiliser la fonction range() pour créer une liste de nombres entiers. On peut ensuite l'utiliser dans une boucle `for` pour répeter une action un certain nombre de fois.

Exemple :
```py
for i in range(10):
    print(i)
```

