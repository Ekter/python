# Cours

1. ordinateurs : couches
   1. langage de programmation 
      1. compilés    ~ rapide
      2. interprétés ~ flexible

```py
print("hello world")
```

   2. assembleur

```asm
 section .text
    global _start

section .data
msg db  'Hello, world!',0xa 
len equ $ - msg        

section .text

_start:


    mov edx,len 
    mov ecx,msg 
    mov ebx,1 
    mov eax,4   
    int 0x80 


    mov ebx,0   
    mov eax,1   
    int 0x80
```

   3. langage machine

```asm
0000000000000000 <_start>:
    0:   ba 0e 00 00 00          mov    $0xe,%edx
    5:   b9 01 00 00 00          mov    $0x1,%ecx
    a:   bb 01 00 00 00          mov    $0x1,%ebx
    f:   b8 04 00 00 00          mov    $0x4,%eax
      14:   cd 80                   int    $0x80
      16:   bb 00 00 00 00          mov    $0x0,%ebx
      1b:   b8 01 00 00 00          mov    $0x1,%eax
      20:   cd 80                   int    $0x80
      ...
```

   4. circuits logiques

```asm
registres trop compliqués
```

2. langage de programmation
   1. passer de l'humain à la machine
   2. peut être n'importe quoi(ex: bf, bash, python, c++)
      1. c++:

```cpp
#include <iostream>
int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
```

      2. python:

```py
print("Hello, world!")
```

      3. bash:

```bash
echo "Hello, world!"
```

      4. brainfuck:

```bf
+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+.

```

   3. Python/ C++ 
      1. interprété/ compilé
      2. vitesse
      3. complexité : typage/ fonctions complexes pas dispo
      4. modules

mention honorable : C/ JAVA/ RUST/ MOJO

Python

.py/ .ipynb / .pyw / .pyi


forme générale code:(imports, def, foncs, pas de ;)

```py
import time

def fonction():
    print(time.time())
    return 37

resultat = fonction()

print(resultat)

```

types : dynamiques
ex : 
```py
var = 1             # int      cpp: int var = 1;
var = "trente-deux" # str           char* var = "trente-deux";
var = True          # bool          short unsigned int var = 1
```

Commentaires : 

```py
#ignorés par python
```

```py
"traités comme une chaine de caractères"
```

```py
"""même en multi- 
ligne"""
```

-> "" pour les docstrings, commentaires intégrés à python


Entiers: `int`

pas grand chose à dire

on peut faire des calculs

on peut changer de base

taille infinie contrairement à int32_t par ex

flottants: `float`

erreurs de calculs à 10^-12 près des fois
```py
Python 3.11.2 (main, May 30 2023, 17:45:26) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/3+1/3+1/3
1.0
>>> 1/2+1/3+1/6
0.9999999999999999
```

si on veut faire des calculs vraiment précis, on peut utiliser le module decimal


chaines de caractères = strings: `str`


```py
s="heLlo woRlD!"
s2='ananas'
s3="""je suis
sur plusieurs
lignes"""
print(s)
print(s2)
print(s3)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.find("l")) # index, commence à 0
```
plein de méthodes pour les strings, on peut les trouver avec `dir(str)`

sous-chaînes:

```py
#  0123456789
s="helloworld"
print(s[1:5]) # [1,5[
print(s[6:]) # [6,fin[
print(s[:5]) # [0,5[
print(s[-3:]) # [fin-3,fin[
```


booléens: `bool`

```py
True
False

print(True and False)
print(True or not False)
print(5==2)
print(5!=2)
print(5>2)
print("a" in "ananas")
```


si on arrive jusque là : 
listes: `list`

```py
l=[1,2,3,4,5]
print(l)
print(l[2])
print(l[1:3])

l.append(6)
l.pop(2)
l.remove(4)
l.insert(2, 4)
```

boucles : `for` / `while`

```py

for i in range(10):
    print(i)

i=10
while i>0:
    print(i)
    i-=1
```