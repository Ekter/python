#programme de Nino Mulac, qui permet de réviser ses tables de multiplication.
from random import randint
def table(nombre,taille=10,entrainement=False):
    if entrainement:
        print("Révision de la table de",nombre,"de 1 à",taille,"en mode entrainement.")
    else:
        print("Révision de la table de",nombre,"de 1 à",taille,"en mode lecture.")
    for i in range(1,taille+1):
        chn=str(nombre)+" * "+str(i)+" = "
        if entrainement and not(randint(0,4)):
            a=int(input(chn))
            if nombre*i==a:
                print("C'est ça!")
            else:
                print("Raté! C'était",nombre*i)
        else:
            print(chn,nombre*i)
test="o"
while test=="o":
    n=int(input("Quelle table réviser? "))
    l=int(input("Jusqu'à combien? "))
    e=input("Mode entrainement?(True/False) ")
    table(n,l,(e=="True"))
    test=input("Continuer?")
