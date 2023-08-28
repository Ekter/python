# Variables en python

On définit une variable avec la syntaxe suivante :

```py
nom_de_la_variable = expression
```

Le nom peut être n'importe quelle chaine de charactères sans espaces, à quelques exceptions près qui sont réservées par python(ex: l'instruction if, si on définit une variable if comment on fait pour utiliser l'instruction if ?)

L'expression peut être n'importe quelle expression, par exemple :

```py
nombre = 1
autre_nombre = 2
somme_des_nombres = a + b
chaine_de_characteres_qui_n_a_rien_a_voir = input("mettre une chaine de caractères svp : ")
```

## Types de variables

Les types les plus importants sont les suivants :

- `int` : entiers
    ```py
    nombre = 37
    ```
- `float` : nombres à virgule
    ```py
    pi = 3.14
    ```
- `str` : chaine de caractères
    ```py
    chaine = "abcd"
    ```

## Fonctions utiles pour les variables

- `print` : affiche une variable
    ```py
    variable = 37
    print(variable)
    ```

- `type` : renvoie le type de la variable
    ```py
    variable_1 = 37
    variable_2 = 3.14
    variable_3 = "abcd"
    type(variable_1) # int
    type(variable_2) # float
    type(variable_3) # str
    ```

- `input` : demande à l'utilisateur d'entrer une valeur, on peut ensuite la stocker dans une variable
    ```py
    exemple_chaine = input("mettre une chaine de caractères svp : ")
    ```

- `int` : convertit une variable en entier
    ```py
    variable_1_str = "37"
    varible_1_int = int(variable_1_str) # 37
    variable_2_float = 3.14
    variable_2_int = int(variable_2_float) # 3
    ```

- `float` : convertit une variable en flottant
    ```py
    variable_1_str = "3.14"
    variable_1_float = float(variable_1_str) # 3.14
    ```

- `str` : convertit une variable en chaine de caractères
    ```py
    variable_1_int = 37
    variable_1_str = str(variable_1_int) # "37"
    variable_2_float = 3.14
    variable_2_str = str(variable_2_float) # "3.14"
    ```

- `==` : vérifie si deux variables sont égales(attention, `=` est l'opérateur d'affectation, il ne faut pas le confondre avec `==`)
    ```py
    variable_1 = 37
    variable_2 = "37"
    variable_1 == variable_2 # False
    ```

- `if` : permet de vérifier une condiiton, si elle est vraie, on exécute le code qui suit, sinon on passe au code suivant
    ```py
    variable_1 = 37
    variable_2 = "37"
    if variable_1 == variable_2:
        print("les variables sont égales")
    else:
        print("les variables ne sont pas égales")
    ```

