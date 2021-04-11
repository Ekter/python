#programme créé par Nino Mulac qui... enfin c'est bon vous voyez là
#fonction moyenne d'une liste
def moyenne(liste):
    somme=0
    for i in liste:
        somme+=i
    return somme/len(liste)
#fin

print(moyenne([1,2,3,4]))