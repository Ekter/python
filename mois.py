#usr/bin/python3
longeurmois=[[31],[28,29],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]]
mois=int(input("numéro du mois"))
if len(longeurmois[mois-1])==1:
    print("il y a ",longeurmois[mois-1][0]," jours dans le mois numéro ",mois,".",sep="")
else:
    print("il y a entre ",longeurmois[mois-1][0]," et ",longeurmois[mois-1][1]," jours dans le mois ",mois,".",sep="")
