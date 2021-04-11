#def de surfaceMur qui donne la surface murale
def surfaceMur(hauteur=2,largeur=5,longueur=5):
    return 2*hauteur*(largeur+longueur)
#fin

#début du programme: on boucle n fois, n le nombre de pièces, et on demande chaque fois les caractéristiques de la pièce.
n=int(input("nombre de pièces: "))
h=float(input("hauteur de la construction:"))
s=0
for i in range(n):
    L=float(input("longueur: "))
    l=float(input("largeur: "))
    s1=surfaceMur(h,l,L)
    print(s1)
    s=s+s1
print(s,"m² à peindre au total")
