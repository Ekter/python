#Programme qui calcule l'écart entre deux jours puis le prix du séjour
#fonction pour récupérer la date depuis le format jj/mm/aa
def lireJourchnverstuple(date):
    return (int(date[0:2]),int(date[3:5]),int(date[6:10]))
#fin

#fonction qui indique si l'annee est bissextile
def anneeBissextileoupas(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return True
    else:
        return False
#fin

#fonction pour le numéro du jour
def donnerNumeroJour(jour,mois,annee):
    if mois>1:
        jour+=31
    if mois>2:
        if anneeBissextileoupas(annee):
            jour+=29
        else:
            jour+=28
    if mois>3:
        jour+=31
    if mois>4:
        jour+=30
    if mois>5:
        jour+=31
    if mois>6:
        jour+=30
    if mois>7:
        jour+=31
    if mois>8:
        jour+=31
    if mois>9:
        jour+=30
    if mois>10:
        jour+=31
    if mois>11:
        jour+=30
    while annee>0:
        if anneeBissextileoupas(annee):
            jour+=366
        else:
            jour+=365
        annee-=1
    return jour
#fin

datededepart=input("date de départ(jj/mm/aaaa):")
datedarrivee=input("date d'arrivee(jj/mm/aaaa):")
prixaujour=int(input("prix au jour:"))
a=lireJourchnverstuple(datedarrivee)
b=lireJourchnverstuple(datededepart)
print(prixaujour*(donnerNumeroJour(a[0],a[1],a[2])-donnerNumeroJour(b[0],b[1],b[2])))
