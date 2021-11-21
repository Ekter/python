#programme écrit par Nino Mulac qui permet de afficher la liste des élèves, de calculer leur moyenne, ou de trouver le major de promo.
#procedure d'affichage
def affichereleves(l,quoi="tous"):
    if quoi=="tous":
        print("Liste des élèves avec leur moyenne: ",l)
    if quoi=="eleves":
        print("Liste des élèves: ",[l[i][0:2] for i in range(len(l))])
    if quoi=="notes" or quoi=="moyennes":
        print("Liste des moyennes des élèves:",[l[i][2] for i in range(len(l))])
    if quoi=="noms":
        print("Liste des noms des élèves:",[l[i][0] for i in range(len(l))])
    if quoi=="prenoms":
        print("Liste des prénoms des élèves:",[l[i][0] for i in range(len(l))])
#fin

#procedure moyenne
def moyenneeleves(l):
    print("La moyenne des élèves est",int(100*sum([i[2] for i in l])/len(l))/100)
#fin

#fonction trouver le major
def major(l):
    return [l[i][2] for i in range(len(l)-1)].index(max([l[i][2] for i in range(len(l)-1)]))
#fin
#sets d'élèves
set1=[["Collavizza","Hélène",6],["Allais","Alphonse",14],["Reed","Lou",12]]#set par defaut
set2=[["Brognart","Denis",15],["Bizel","Edgar",17],["Dellile","Alex",17],["","Apoorva",12],["Mulac","Nino",14]]#notes au QCM d'EnvInfo1
set3=[["","Skander",12],["","Loic",42],["Mulac","Nino",37],["Calleya","Enzo",37],["Chan","Darina",34+35]]#nombres préférés des interessés
sets=[set1,set2,set3]
senssets={1:"set par défaut",2:"notes au QCM d'EnvInfo1",3:"nombres préférés"}

print("\n"*3,"Gestion des listes d'élèves","\n"*3)
choix=input("Garder le set d'élèves par défaut ? (Hélène, Alphonse et Lou) (O/n)")
if choix.lower()=="n" or choix.lower()=="no" or choix.lower()=="non":
    print("\n"*2,"Quel set de données voulez-vous utiliser?","\n"*2)
    for settemp in range(len(sets)):
        print(settemp+1,")",sets[settemp]," : ",senssets.get(settemp+1),"\n")
    choix2=int(input("Quel set utiliser ? "))
    setdefinitif=sets[int(choix2)-1]
else:
    setdefinitif=set1
print("\n"*2,setdefinitif,"\n"*2)
continuer=1
while continuer==1:
    print("Actions possibles:","\n"*2,"1: afficher les élèves","\n","2: calculer la moyenne de la classe","\n","3: trouver le major","\n","4: aide","\n","5: sortir","\n"*2)
    a=input("Que voulez-vous faire?")
    print("\n")
    if a[0]=="1":
        liste=a.split(" ")
        if len(liste)>=2:
            for i in liste[1:]:
                affichereleves(setdefinitif,i)
        else:
            affichereleves(setdefinitif)
    if a=="2":
        moyenneeleves(setdefinitif)
    if a=="3":
        print("Le major est ",setdefinitif[major(setdefinitif)][1]," ",setdefinitif[major(setdefinitif)][0]," avec une note de ",setdefinitif[major(setdefinitif)][2],".",sep="")
    if a=="4":
        print("Ce programme est une aide au traitement d'informations sur des listes d'élèves, qui permet de trouver la moyenne, et le major d'un groupe. ")
    if a=="5":
        continuer=0
    print("\n")
