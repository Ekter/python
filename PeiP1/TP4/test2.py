#Programme qui calcule l'écart entre deux jours puis le prix du séjour
#fonction pour récupérer la date depuis le format jj/mm/aa
def lireJourchnverstuple(date):
    return (int(date[0:2],int(date[2:4]),int(date[4:6])))
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
    if m>1:
        jour+=31
    if m>2:
        if anneeBissextileoupas(annee):
            jour+=29
        else:
            jour+=28
    if m>3:
        jour+=31
    if m>4:
        jour+=30
    if m>5:
        jour+=31
    if m>6:
        jour+=30
    if m>7:
        jour+=31
    if m>8:
        jour+=31
    if m>9:
        jour+=30
    if m>10:
        jour+=31
    if m>11:
        jour+=30
    while annee>0:
        if anneeBissextileoupas(annee):
            jour+=366
        else:
            jour+=365
    return jour
#fin

datededepart=input("date de départ(jjmmaaaa):")
datedarrivee=input("date d'arrivee(jjmmaaaa):")
print(donnerNumeroJour(lireJourchnverstuple(datedarrivee)),donnerNumeroJour(lireJourchnverstuple(datededepart)))