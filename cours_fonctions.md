# Python - Fonctions

Les fonctions sont les briques de la programmation. Elles permettent de découper un programme en plusieurs parties, ce qui permet de le rendre plus lisible et plus facile à modifier.
Une fonction est un bloc de code qui prend des paramètres en entrée et renvoie un résultat en sortie.


## Définir une fonction

On définitune fonction avec le mot clef `def`:
```py
def nom_de_la_fonction(parametre_1, parametre_2, ...):
    # code de la fonction
    return resultat

nom_de_la_fonction(valeur_1, valeur_2, ...)
```

Les parametres peuvent être des variables, des valeurs, ou des fonctions.
On peut passer un parametre par défault avec =, dans ce cas là il sera facultatif lors de l'appel de la fonction.

```py
def nom_de_la_fonction(parametre_1, parametre_2=0):
    # code de la fonction
    return resultat

nom_de_la_fonction(valeur_1)
```

Par exemple, la fonction `int` prend en paramètre une variable et renvoie la valeur de cette variable convertie en entier. Elle a un parametre facultatif : base, qui est égal à 10 par défaut.
Sa définition ressemble à ça :

```py
def int(variable, base=10):
    # code de la fonction
    return resultat
```

Ce qui permet de l'utiliser de différentes façons :

```py
int("123") # 123
int("123", 2) # 7
int("123", 16) # 291
```


## Renvoyer un résultat

Renvoyer un résultat à la fin de l'éxecution d'une fonction se fait avec le mot clef `return`. On peut récupérer ce résultat en stockant l'appel de la fonction dans une variable.

```py
def fonction():
    return 4

a = fonction()
print(a) # 4
```

On peut renvoyer plusieurs résultats en les séparant par des virgules.

```py
def fonction():
    return 4, "5"

a, b = fonction()
print(a) # 4
print(b) # "5"
```

Si on ne renvoie rien, la fonction renvoie `None` par défaut.

```py
def fonction():
    print("coucou")

a=fonction() # print "coucou"
print(a) # None
```

### Exercices

* Ecrire une fonction qui prend en paramètre un nombre et renvoie son carré.
* Ecrire une fonction qui prend en paramètre un nombre et une chaine de caractère et renvoie une liste contenant la chaine de caractères répétée n fois jusqu'au nombre donné, avec n l'index de la chaine dans la liste.
Exemple: `fonction(3, "a")` renvoie `["a", "aa", "aaa"]`
* Ecrire une fonction qui prend en paramètre une liste de formes et les dessine, en utilisant le module `turtle` de python.
  * Exemple d'entrée  : `["carre", "triangle", "cercle"]`
  * On peut pimenter en prenant en entrée d'autres paramètres, comme la taille, la couleur, etc...

* Ecrire une fonction qui prend en paramètre une liste de nombres et renvoie la somme de ces nombres.


## Fonctions récursives

Une fonction peut s'appeller elle même. On parle de fonction récursive.
C'est utile pour définir des suites récursives par exemple.

Attention toutefois, il faut que la fonction s'arrête à un moment donné, sinon elle s'appellera elle même à l'infini et le programme ne pourra pas continuer.
La limite de nombre de fois qu'une fonction peut s'appeller elle même est fixée par la limite de récursion du langage. En python, cette limite est de 1000 appels.


exemple:
```py
def somme_jusqu_a_n(n):
    if n == 0:
        return 0
    else:
        return n + somme_jusqu_a_n(n-1)

print(somme_jusqu_a_n(5)) # 5 + (4 + (3 + (2 + (1 + (0))))) = 15
```

### Exercices

* Ecrire une fonction qui prend en paramètre un nombre et renvoie la somme de tous les carrés des nombres de 1 à ce nombre.
* Ecrire une fonction qui calcule le n-ième terme de la suite de Fibonacci. (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)
  * on peut commencer par faire deux appels récursifs dans la fonction, puis les combiner pour n'en faire qu'un seul pour optimiser l'éxecution parce que c'est vraiment lent sinon...


## Plus sur les signatures de fonctions

On peut définir des fonctions avec un nombre de paramètres variable. Pour cela, on utilise le symbole `*` devant le nom du paramètre. Cela permet de passer un nombre variable de paramètres à la fonction, qui seront stockés dans une liste.
Par exemple, la fonction print peut prendre autant d'arguments que souhaité, et les affiche tous à la suite. Voici sa signature :


```py
def print(*args, sep=' ', end='\n', file=None):
    # code de la fonction
    for arg in args:
        ... # print arg
```

`sep` permet de définir le séparateur entre les arguments, `end` le caractère à la fin de la ligne, et `file` le fichier dans lequel écrire. Par défaut, `sep` vaut un espace, `end` vaut un retour à la ligne, et `file` vaut la sortie standard (la console).

On peut typer une fonction pour faciliter la lecture et permettre à l'IDE de nous aider à l'utiliser correctement, mais ce sont juste des annotations, elles peuvent juste servir à l'optimisation dans certains cas, sinon elles ne sont pas utilisées par python.

```py
def cube(nombre: int) -> int:
    return nombre * nombre * nombre
```


On peut aussi insérer une chaine de caractères après la définition d'une fonction pour la documenter. C'est ce qui s'affiche quand on fait `help(nom_de_la_fonction)`.

```py
def cube(nombre: int) -> int:
    """Renvoie le cube du nombre donné en paramètre"""
    return nombre * nombre * nombre

help(cube) # fonction cube(nombre: int) -> int
           # Renvoie le cube du nombre donné en paramètre
```
