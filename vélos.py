#/usr/bin/python3
print("Location de vélos!")
heures=int(input("Combien d'heures voulez vous louer? "))
abonnement=input("Avez vous un abonnement?")
prix=0
for i in range(1,heures+1):
    if i<=2:
        prix=prix+3
    if i>2:
        prix=prix+5
if (abonnement=="oui" or abonnement=="O" or abonnement=="1")==False:
    prix=prix+2
print("ça coute "+str(prix)+" euros.")
