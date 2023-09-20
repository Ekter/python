# Python - Fichiers textes

Manipuler des fichiers est intéressant pour enrigistrer des données, ou pour lire des données qui ont été enregistrées.
Il existe une pléthore de types de fichier, et chacun a ses spécificités. Nous allons nous intéresser ici aux fichiers textes, qui sont les plus simples à manipuler.
Les fichiers textes sont les fichiers que l'ont peut ouvrir avec n'importe quel éditeur de texte, comme le bloc-notes de Windows.
Par exemple, les fichiers `.txt`, `.py`, `.gcode`, `.csv` sont des fichiers textes.

Pour l'exemple, on va considérer un fichier `fichier.txt` situé au même endroit que le programme qui contient le texte suivant:

```
Bonjour,
Je suis un fichier texte de trois lignes.
La constante de Plik est 37 très exactement.
```

## Ouvrir un fichier

Pour ouvrir un fichier, on utilise la fonction `open`. Elle prend en paramètre le chemin du fichier, et le mode d'ouverture.
Il faut préciser le chemin du fichier, c'est-à-dire son emplacement sur le disque dur. Si le fichier est dans le même dossier que le programme, on peut juste mettre le nom du fichier.
Les modes d'ouverture les plus importants sont:
* `r`: ouverture en lecture seule
* `w`: ouverture en écriture seule. Si le fichier existe déjà, il sera écrasé.
* `a`: ouverture en écriture seule. Si le fichier existe déjà, on écrit à la fin du fichier.
On peut cumuler les modes (`rw` par exemple pour lire et écrire)


```py
fichier = open("fichier.txt", "r")
# le fichier est ouvert en lecture seule
```

Il est important de fermer le fichier après utilisation, pour éviter des problèmes de mémoire. Pour cela, on utilise la méthode `close` une fois qu'on a fini de lire ou d'écrire dans le fichier.
En pratique, le système d'exploitation ferme automatiquement les fichiers à la fin du programme, mais il est préférable de le faire soi-même.

```py
fichier = open("fichier.txt", "rw")
# opérations sur le fichier
fichier.close()
```

## Lire un fichier

Il existe différentes fonctions pour lire un fichier. La plus simple est `read`, qui renvoie tout le contenu du fichier sous forme de chaîne de caractères.

```py
fichier = open("fichier.txt", "r")
contenu = fichier.read()
print(contenu)
# Bonjour,
# Je suis un fichier texte de trois lignes.
# La constante de Plik est 37 très exactement.
fichier.close()
```

On peut aussi lire le fichier ligne par ligne, avec la méthode `readline`. Elle renvoie une ligne à chaque appel, et renvoie une chaîne vide quand on arrive à la fin du fichier.

```py
fichier = open("fichier.txt", "r")
ligne = fichier.readline()
while ligne != "":
    print(ligne)
    ligne = fichier.readline()
# Bonjour,
# Je suis un fichier texte de trois lignes.
# La constante de Plik est 37 très exactement.
fichier.close()
```
Le faire avec une boucle `for` n'est pas possible si on ne sait pas combien de lignes il y a dans le fichier.
Toutefois, il existe une fonction `readlines` qui renvoie une liste de toutes les lignes du fichier.
Elle est donc plus adaptée à une boucle `for`.

```py
fichier = open("fichier.txt", "r")
lignes = fichier.readlines()
for ligne in lignes:
    print(ligne)
# Bonjour,
# Je suis un fichier texte de trois lignes.
# La constante de Plik est 37 très exactement.
fichier.close()
```


## Écrire dans un fichier

Pour écrire dans un fichier, on utilise la méthode `write`. Elle prend en paramètre une chaîne de caractères, et l'écrit dans le fichier.
Il faut penser à ajouter les caractères de retour à la ligne `\n` si on veut écrire plusieurs lignes.

```py
fichier = open("fichier.txt", "a")
fichier.write("Ceci est une ligne ajoutée au fichier\n")
fichier.close()

fichier = open("fichier.txt", "r")
contenu = fichier.read()
print(contenu)
# Bonjour,
# Je suis un fichier texte de trois lignes.
# La constante de Plik est 37 très exactement.
# Ceci est une ligne ajoutée au fichier
```

Il est aussi possible d'écrire plusieurs lignes à la fois avec la méthode `writelines` de la même manière que `readlines`. Elle prend en paramètre une liste de chaînes de caractères, et les écrit dans le fichier.

```py
fichier = open("fichier.txt", "w")
fichier.writelines(["Ceci est la première ligne du fichier\n", "Et voici la deuxième\n", "Et la constante de Plik est toujours 37\n"])
fichier.close()

fichier = open("fichier.txt", "r")
contenu = fichier.read()
print(contenu)

# Ceci est la première ligne du fichier
# Et voici la deuxième
# Et la constante de Plik est toujours 37
```

## Exercice

* Faire un programme qui demande à l'utilisateur un nombre, et qui écrit dans un fichier `resultats.txt` la liste des nombres premiers jusqu'à ce nombre, chacun sur une ligne(réutiliser le programme des nombres premiers).

* Faire un programme qui demande à l'utilisateur deux noms de fichiers et qui copie le contenu du premier dans le deuxième.

* Faire un programme qui lit tout un fichier Gcode et affiche toutes ses commandes sous forme de dictionnaire(réutiliser le programme de gcode).

* Faire un programme qui fusionne tous les programmes du dossier actuel dans un fichier de sortie donné par l'utilisateur.
  * On peut utiliser la fonction `listdir` du module `os` pour lister les fichiers et dossiers du dossier actuel.
  * exemple: `os.listdir(".")` renvoie la liste des fichiers et des dossiers contenus dans le dossier actuel. On peut trouver si un élément est un fichier ou un dossier en regardant si le nom contient un point ou pas pour simplifier: `if "." in element: # c'est un fichier`



## Pour aller plus loin

Plutôt que de faire `fichier.close()` à chaque fois, on peut utiliser le mot-clé `with` pour ouvrir un fichier. Il se chargera de fermer le fichier à la fin du bloc d'instructions.

```py
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
    # Bonjour,
    # Je suis un fichier texte de trois lignes.
    # La constante de Plik est 37 très exactement.
# le fichier est fermé
```

Pour ouvrir certains types de fichiers textes, il existe des modules qui font tout le travail de traitement pour nous. Pax exemple, pour les fichiers qui ont des données organisées en séries, comme les fishiers CSV, on peut utiliser le module `pandas`. Il permet de lire et d'écrire des fichiers CSV très facilement, ainsi que de faire de la modification de données.


C'est le cas aussi pour le Gcode, avec le module `gcodeparser` qui permet de lire des fichiers Gcode et de récupérer les commandes sous forme de dictionnaires.
Ce module n'est pas installé par défaut en Python, on verra la prochaine fois comment l'installer(sinon tu vas tricher pour les exercices :p)
