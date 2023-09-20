# Python - Dictionnaires

Les dictionnaires sont un moyen très pratique de stocker des données. Ils permettent de stocker des couples clé/valeur, et de retrouver une valeur à partir de sa clé.

## Définir un dictionnaire

On définit un dictionnaire avec des accolades `{}`. On peut y mettre des couples clé/valeur séparés par des virgules `,`.

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}
```

Les clés et les valeurs peuvent être de n'importe quel type, et peuvent être mélangées.



```py
dictionnaire = {"cle1": "valeur1", 2: "valeur2", "cle3": 3}
```

Pour récuperer une valeur en ayant la clé, on utilise des crochets `[]`(comme pour les listes).

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}
print(dictionnaire["cle1"]) # valeur1
```

Par contre, si on essaie de récuperer une valeur avec une clé qui n'existe pas, on obtient une erreur.

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}

print(dictionnaire["cle3"]) # KeyError: 'cle3'
```

Pour éviter cette erreur, on peut utiliser la méthode `get` qui renvoie `None` si la clé n'existe pas.

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}

print(dictionnaire.get("cle3")) # None
```

Mais attention, envoyer None dans le reste du programme peut causer des problèmes, si notre programme s'attendait à trouver un certain type de données.



On peut aussi ajouter des valeurs plus tard à un dictinnaire.

```py
dictionnaire = {}
dictionnaire["cle1"] = "valeur1"
dictionnaire["cle2"] = "valeur2"
```

## Parcourir un dictionnaire

On peut vérifier si une clé est dans un dictionnaire en utilisant le mot clef `in`.

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}

if "cle1" in dictionnaire:
    print("La clé 'cle1' est dans le dictionnaire")
```

On peut parcourir un dictionnaire avec une boucle `for`. Par défaut, la boucle parcourt les clés.

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}

for cle in dictionnaire:
    print(cle) # cle1, cle2
```
Pour afficher les valeurs dans la boucle il suffit donc de récuperer la valeur à partir de la clé.

```py
dictionnaire = {"cle1": "valeur1", "cle2": "valeur2"}

for cle in dictionnaire:
    print(dictionnaire[cle]) # valeur1, valeur2
```

Exercices:

Faire un programme qui parcourt un dictionnaire(contenant uniquement des chaines de caractères) et affiche les clés et les valeurs de la façon dont on définit les dictionnaires:

`{"cle1": "valeur1", "cle2": "valeur2"}`

Indice: le parametre `end` de la fonction `print` permet de changer le caractère qui est affiché à la fin de la ligne. Par défaut, c'est un retour à la ligne `\n`. On peut faire print("coucou", end="") pour ne pas avoir de retour à la ligne, ce qui permet de faire plusieurs print à la suite sur la même ligne.



Gros exercice:

On va essayer de lire du gcode et de le transformer en un dictioannaire pour l'analyser plus facilement.

Le gcode ressemble à ça :
```gcode
G1 X10 Y-2.5 ; this is a comment
```
La commande est `G1`, et les paramètres sont `X10` et `Y-2.5`. Les commentaires commencent par `;` et vont jusqu'à la fin de la ligne.

Le but est d'afficher un dictionnaire comme:
```py
{"G": "1", "X": "10", "Y": "-2.5"}
```
(on devrait traiter le G1 séparément, mais ce sera plus facile comme ça.)

On peut ignorer les commentaires pour l'instant, donc la première étape est de séparer les commandes des commentaires. Il faut vérifier si le caractère `;` est dans la ligne, et si oui, ne garder que ce qui est avant.

Indice: utiliser la méthode split sur la chaine de caractères, qui renvoie la liste des éléments séparés par le caractère donné en paramètre.


Ensuite, il faut séparer les paramètres de la commande. Encore une fois, split avec l'espace comme paramètre devrait faire l'affaire.

Enfin, il faut séparer les paramètres en clé/valeur.
La clé est toujours la première lettre du paramètre, et la valeur est le reste du paramètre.
Donc il va falloir utiliser des sous-chaines de caractères.

Pour ce faire, il faut utiliser les crochets directement sur la chaine de caractères, comme pour les listes et les dictionnaires.
            -1
```py     0123
chaine = "abcd"
print(chaine[0]) # a
print(chaine[1]) # b
print(chaine[2]) # c
print(chaine[3]) # d
```

Pour récupérer une sous chaine on peut utiliser les `:`:

```py
chaine = "abcd"
print(chaine[1:3]) # bc car on commence à l'index 1 et on s'arrête à l'index 3(exclu)
```

Et si on veut aller jusqu'à la fin peu importe la taille :

```py
chaine = "abcd"
print(chaine[1:]) # bcd
```

On peut aussi l'utiliser dans l'autre sens :

```py
chaine = "abcd"
print(chaine[:3]) # abc
```

Et on peut aussi utiliser des nombres négatifs pour partir de la fin :

```py
chaine = "abcd"
print(chaine[-1]) # d
```

Bonus : ça marche pareil sur les listes :

```py
liste = [1, 2, 3, 4]
print(liste[1:3]) # [2, 3]
```

Une fois la clé et la valeur séparées, il faut les ajouter au dictionnaire, et c'est bon, on a réussi à transformer une ligne de gcode en un dictionnaire.


```py
n=37

c = 3
while c < n:
    print(c)
    c = c + 2

for c in range(3, n, 2):
    print(c)
```
