#Programme créé par Nino Mulac et Hugo Durand, visant à produire une variante du jeu de Nim, pour le projet de programmation impérative
#On part du principe que une quille seule est une liste de la forme [n,n+1], pour que fin-début soit le nombre de quilles de la ligne.
#Importations: turtle pour l'interface graphique, pynnput pour les controles au clavier, time pour les delais, et random pour l'aléatoire
from turtle import *                            #pour l'interface graphique
from pynput.keyboard import Key, Controller     #pour les contrôles au clavier
from time import sleep                          #pour les délais, mais pas encore utilisés
from random import randint, choice, random      #pour l'aléatoire
from dessinblocs import *                       #pour les graphismes
#fonction afficherquilles : par une liste en compréhension, on parcourt les sous listes de c, et on join les sous-chaines, puis on y ajoute le début et la fin de la ligne de quilles, avec des quilles tombées.
def afficherquilles(c,nlim):
    return "-"*(c[0][0]-1)+"".join(["-"*(c[i][0]-c[i-1][1])+"|"*(c[i][1]-c[i][0])+"-"*(nlim-c[len(c)-1][1]) for i in range(0,len(c))])
#fin

#fonction ordijoue: si la ligne où l'ordinateur veut jouer est vidable, il la vide
def ordijoue(q):
    n=randint(1,len(quilles))-1
    a=str(n+1)+":"
    if quilles[n][1]-quilles[n][0]<=2:
        a+="M"
    else:
        a+=choice(["G","M","D"])
    return a
#fin

#fonction joueurjoue, boucle tant que c'est pas bon
def joueurjoue(q):
    Cpasbon=1
    while Cpasbon!=0:
        a=textinput("Jeu des quilles","Où voulez-vous jouer?")
        Cpasbon=0
        if a.find(":")==-1:
            print("Il manque le ':'!")
            Cpasbon+=1
        print(a[:a.find(":")])
        if a[:a.find(":")].isnumeric():
            if not(int(a[:a.find(":")])>=1 and int(a[:a.find(":")])<=len(q)):
                print("Cette liste est en dehors des bornes!")
                Cpasbon+=1
        else:
            print("Ce n'est pas un nombre!")
            Cpasbon+=1
        print(a[a.find(":")+1:])
        if not(a[a.find(":")+1:]=="G" or a[a.find(":")+1:]=="M" or a[a.find(":")+1:]=="D"):
            print("Ce n'est pas un choix valide!")
            Cpasbon+=1
    return a
#fin

#fonction jouer()
def jouer(quilles,a):
    nlignejeu=int(a[:a.find(":")])
    lettrejeu=a[a.find(":")+1:]
    print(nlignejeu,lettrejeu,quilles)
    sousquille=quilles[nlignejeu-1]
    if lettrejeu!="M":
        if lettrejeu=="G":
            sousquille[0]+=1
            if sousquille[0]>=sousquille[1]:
                quilles.remove(sousquille)
        if lettrejeu=="D":
            sousquille[1]-=1
            if sousquille[1]<=sousquille[0]:
                quilles.remove(sousquille)
    else:
        if sousquille[1]-sousquille[0]<=2:
            quilles.remove(sousquille)
        else:
            if sousquille[1]-sousquille[0]==3:
                quilles=quilles[:nlignejeu-1]+[[int((sousquille[1]+sousquille[0])/2)+1,sousquille[1]]]+quilles[nlignejeu:]
            else:
                quilles=quilles[:nlignejeu-1]+[[sousquille[0],int((sousquille[1]+sousquille[0])/2)-1]]+[[int((sousquille[1]+sousquille[0])/2)+1,sousquille[1]]]+quilles[nlignejeu:]
    return(quilles)
#fin

def couvrirlecran():
    for i in range(-300,300,10):
        for j in range(-300,300,10):
            carreplein20((random(),random(),random()),i,j)
tracer(0)
couvrirlecran()
#Initialisations:
nlimitquilles=randint(5,37)
quilles=[[1,nlimitquilles]]
joueur=0                                        #joueur=0:ordi; joueur=1:humain, on alterne au début de la boucle.

while len(quilles)>0:                           #boucle
    joueur=-1*joueur+1                          #on passe la main
    afficherquillesbleuourouge(afficherquilles(quilles,nlimitquilles),-100,joueur*20)
    if joueur==1:                               #
        a=joueurjoue(quilles)
    else:
        a=ordijoue(quilles)
    quilles=jouer(quilles,a)
if joueur==1:
    print("Bravo! Tu as gagné!")
else:
    print("Dommage... l'ordi qui joue presque au hasard t'a battu... En fait t'es vraiment nul.")