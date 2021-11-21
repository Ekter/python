#Programme qui indique le lendemain, écrit par Nino Mulac

#fonction qui indique si l'annee est bissextile
def anneeBissextileoupas(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return True
    else:
        return False
#fin

#fonction qui donne le nombre de jours d'un mois(1-12)
def jourMois(mois,annee=1):
    if mois==2 and anneeBissextileoupas(annee):
        return 29
    else:
        return [31,28,31,30,31,30,31,31,30,31,30,31][mois-1]
#fin

#fonction qui donne le lendemain
def donnerLendemain(jour,mois,annee):
    jour+=1
    if jour>jourMois(mois,annee):
        jour=1
        mois+=1
        if mois>12:
            annee+=1
            mois=1
    return jour,mois,annee
#fin

print(donnerLendemain(37,12,2020))