#programme écrit par Nino Mulac qui fait le produit matriciel d'une matrice et d'un vecteur
import lireListe

#fontion qui multiplie et additionne
def produitligne(liste1,liste2):
    return sum([liste1[n]*liste2[n] for n in range(len(liste1)-1)])

continuer="o"
while continuer!="n":
    taille=lireListe.lireListeEntier("Taille de la matrice:")
    matrice=[]
    for k in range(taille[0]):
        matrice+=[lireListe.lireListeEntier(str(k+1)+" ème ligne: ")]
    for k in matrice:
        if len(k)!=taille[1]:
            print("c'est pas bon!")
    vecteur=lireListe.lireListeEntier("Vecteur de taille "+str(taille[1])+" : ")
    resultat=[]
    for k in matrice:
        resultat.append(produitligne(k,vecteur))
    print(resultat)
    continuer=input("Continuer(o/n): ")
