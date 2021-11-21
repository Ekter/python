import random
"""#usr/bin/python3
longeurmois=[[31],[28,29],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]]
mois=int(input("numéro du mois"))
if len(longeurmois[mois-1])==1:
    print("il y a ",longeurmois[mois-1][0]," jours dans le mois numéro ",mois,".",sep="")
else:
    print("il y a entre ",longeurmois[mois-1][0]," et ",longeurmois[mois-1][1]," jours dans le mois ",mois,".",sep="")
"""
def troisnplusun(n):
    if n%2==0:
        return n//2
    return 3*n+1

po=1
n=1
while True:
    i=n
    k=i
    while i!=1:
        i=troisnplusun(i)
        if i>10**po:
            print(10**po)
            po+=1
        if i<k:
            break
    n+=1
    