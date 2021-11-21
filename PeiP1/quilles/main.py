#Programme créé par Nino Mulac et Hugo Durand, visant à produire une variante du jeu de Nim, pour le projet de programmation impérative
#On part du principe que une quille seule est une liste de la forme [n,n+1], pour que fin-début soit le nombre de quilles de la ligne.
#Importations: turtle pour l'interface graphique, pynnput pour les controles au clavier, time pour les delais, et random pour l'aléatoire
import turtle
from dessinblocs import afficherquilles
from tkinter.constants import CENTER
from turtle import *                                #pour l'interface graphique
from pynput.keyboard import Key, Controller         #pour les contrôles au clavier
from time import sleep                              #pour les délais, mais pas encore utilisés
from random import randint, choice                  #pour l'aléatoire
from dessinblocs import *
from math import pi,sin,cos
from logo import *
#fonction ordijoue: si la ligne où l'ordinateur veut jouer est vidable, il la vide
def ordijoue(q):
    n=randint(1,len(quilles))-1                     #Choix de la sous ligne
    a=str(n+1)+":"                                  #ajout du ":"
    if quilles[n][1]-quilles[n][0]<=2:              #si la sousligne a une longueur de 2 ou moins on la prend en entier, pour éviter que l'ordi perde bêtement 
        a+="M"                                      #le milieu pour prendre les sous ligne de longueur 2 en entier
    else:                                           #dans les autres cas on choisit au hasard
        a+=choice(["G","M","D"])                    #entre gauche, milieu, et droite
    return a                                        #retour de la chaîne du jeu de l'ennemi
#fin
def comparerafficherquilles(listequille1,listequille2,nlim):
    l1=afficherquilles(listequille1,nlim)
    l2=afficherquilles(listequille2,nlim)
    listerésultats=[]
    for i in range(nlim-1):
        if l1[i]!=l2[i]:
            listerésultats.append(i)
    return listerésultats

#fonction joueurjoue, boucle tant que c'est pas bon
def joueurjoue(q,a):
    Cpasbon=1                                       #Cpasbon est une variable pour boucler tant que la réponse de l'utilisateur
    while Cpasbon!=0:                               #boucle tant que c'est pas bon
        if a!="":
            if len(a)<10:
                a=textinput("Jeu des quilles","""Où voulez-vous jouer?
        L'ordinateur a joué """+a)#input du choix de jeu
            else:
                a=textinput("Jeu des quilles",a+"\nOù voulez-vous jouer?")#input du choix de jeu
        else:
            a=textinput("Jeu des quilles","Où voulez-vous jouer?")
        if a=="stop":
            bye()
        Cpasbon=0                                   #initialisation de Cpasbon avant les tests de valabilité de la réponse
        pos=a.find(":")                             #pos stocke la position du ":"
        if pos==-1:                                 #si il n'y a pas de ":" dans la réponse de l'utilisateur
            print("Il manque le ':'!")              #alors on le lui dit
            Cpasbon+=1                              #et on modifie Cpasbon pour lui redemander où jouer
        if a[:pos].isnumeric():                     #si c'est bien un nombre que l'utilisateur entre
            if not(int(a[:pos])>=1 and int(a[:pos])<=len(q)):#alors on vérifie qu'il corresponde à une sous ligne
                print("Cette liste est en dehors des bornes!")#dans le cas contraire on le lui dit
                Cpasbon+=1                          #et on modifie Cpasbon pour lui redemander où jouer
        else:                                       #si ce n'est pas un nombre
            print("Ce n'est pas un nombre!")        #alors on le lui dit
            Cpasbon+=1                              #et on modifie Cpasbon pour lui redemander où jouer
        lettresjeu=a[a.rfind(":")+1:]                        #on assigne lettrejeu
        print(lettresjeu)
        if not(lettresjeu=="G" or lettresjeu=="M" or lettresjeu=="D"):#on vérifie que c'est bien G, M, ou D
            print("Ce n'est pas un choix valide!")  #sinon on le lui dit
            Cpasbon+=1                              #et on modifie Cpasbon pour lui redemander où jouer
    return a                                        #si les tests sont passés on retoourne le choix de jeu
#fin

#fonction jouer()
def jouer(quilles,a):
    nlignejeu=int(a[:a.find(":")])                  #on récupère la ligne où l'utilisateur veut jouer(avant le ":") et on l'assigne à nlignejeu 
    lettrejeu=a[a.find(":")+1:]                     #on récupère l'endroit où l'utilisateur veut jouer(après le ":") et on l'assigne à lettrejeu
    sousquille=quilles[nlignejeu-1]                 #on récupère la sous ligne de quille associée à nlignejeu e on l'assigne à sousquille
    if lettrejeu!="M":                              #si on joue au bord
        if lettrejeu=="G":                          #si on joue à gauche
            sousquille[0]+=1                        #on ajoute 1 au début de la ligne(on enlève la première quille)
        if lettrejeu=="D":                          #si on joue à droite
            sousquille[1]-=1                        #on enlève 1 à la fin de la ligne(on enlève la dernière quille)
        if sousquille[1]<=sousquille[0]:            #si la sous ligne est vide
            quilles.remove(sousquille)              #on la supprime
    else:                                           #sinon(on joue au milieu)
        if sousquille[1]-sousquille[0]<=2:          #si la liste a une longueur de 2 ou moins
            quilles.remove(sousquille)              #on la supprime
        elif sousquille[1]-sousquille[0]==3:        #sinon si elle a une longueur de 3
            quilles=quilles[:nlignejeu-1]+[[int((sousquille[1]+sousquille[0])/2)+1,sousquille[1]]]+quilles[nlignejeu:]#on supprime les deux premiers de la sous ligne
        else:                                       #sinon(longueur>3)
            quilles=quilles[:nlignejeu-1]+[[sousquille[0],int((sousquille[1]+sousquille[0])/2)-1]]+[[int((sousquille[1]+sousquille[0])/2)+1,sousquille[1]]]+quilles[nlignejeu:]#on coupe la sous ligne en 2
    return(quilles)                                 #on retourne la liste des quilles
#fin
#Initialisations:
a=""
t=1
tortueecran1=Turtle(shape="circle",undobuffersize=0,visible=True)
tortueecran2=Turtle(shape="circle",undobuffersize=0,visible=True)
tortueecran1.turtlesize(0.5,0.5)
tailleinitialex=0
tailleinitialey=0
ecranquilles=Screen()
boule(ecranquilles,1,0,0)
cafe(ecranquilles,1,0,0)
calculatrice(ecranquilles,1,0,0)
chat(ecranquilles,1,0,0)
#chaussette(ecranquilles,1,0,1)
nuage(ecranquilles,1,0,0)
coca(ecranquilles,1,0,0)
pion(ecranquilles,1/4,0,0)
couteau(ecranquilles,1,0,0)
dé(ecranquilles,1,0,0)
#livrequdeux(ecranquilles,1,0,1)
#livretrsept(ecranquilles,1,0,1)
masque(ecranquilles,1,0,0)
pate(ecranquilles,1,0,0)
pokeball(ecranquilles,1,0,0)
PQ(ecranquilles,1,0,0)
masterpomme(ecranquilles,1,0,0)
tournevis(ecranquilles,1,0,0)
wumpus(ecranquilles,1,0,0)
tomate(ecranquilles,1,0,0)
voiture(ecranquilles,1,0,0)
halteres(ecranquilles,1,0,0)
caleçon(ecranquilles,1,0,0)
lit(ecranquilles,1,0,0)
nuage(ecranquilles,1,0,0)
cadismiroir(ecranquilles,1,0,0,)
cadis1=Turtle("cadis",0,True)
cadis2=Turtle("cadismiroir",0,True)
cadis1.ht()
cadis2.ht()
tortueecran1.penup()
tortueecran2.penup()
tortueecran1.pencolor("#ffffff")
tortueecran1.dot(800)
tortueecran1.pencolor("#000000")

gotopourcent(50,40,tortueecran1)
tortueecran1.write("Bienvenue au Supermaché Coco!",align=CENTER,font=("Arial",int(window_height()/25),"normal"))
tortueecran1.showturtle()
tortueecran2.showturtle()
logo(0.5,0,100,tortueecran1)
tortueecran1.penup()
tortueecran1.pencolor("black")
for i in range(101):
    gotopourcent(50+5*cos(i/100*4*pi+pi/2),30+5*sin(i/100*4*pi+pi/2),tortueecran1)
    gotopourcent(50+5*cos(i/50*4*pi+pi/2),30+5*sin(i/50*4*pi+pi/2),tortueecran2)
    update()

tortueecran1.hideturtle()
tortueecran2.hideturtle()

listequillespossibles=["lit","pion","halteres","caleçon","voiture","tomate","boule","cafe","calculatrice","chat","coca","couteau","de","masque","pate","pq","masterpomme","tournevis","wumpus"]
listequilles=[]
listetortuestempquilles=[]
ecranquilles=Screen()
for _ in range(3):
    k=randint(12,15)
    ltemp=[]
    ltempquilles=[]
    for i in range(k):
        ltemp.append(choice(listequillespossibles))
        ltempquilles.append(Turtle(shape=ltemp[-1],undobuffersize=0,visible=True))
    listequilles.append(ltemp)
    listetortuestempquilles.append(ltempquilles)

listetortuesnuages=[]
for manche in range(3):
    quilles=[[1,len(listequilles[manche])]]                         #on crée la liste des quilles
    joueur=0                                            #joueur=0:ordi; joueur=1:humain, on alterne au début de la boucle.
    tracer(0)
    print(listequilles,quilles)
    quillesavant=quilles.copy()
    while len(quilles)>0:                               #boucle tant qu'il reste des quilles
        changerquilles(listequilles,quilles,manche,listetortuestempquilles)
        for tanim in range(10):
            if tailleinitialex!=window_width() or tailleinitialey!=window_height():
                tailleinitialex=window_width()
                tailleinitialey=window_height()
                afficherétagere(listequilles,quilles,manche,listetortuestempquilles,cadis1,cadis2)
            t+=0.3
            print(undobufferentries(),window_width())
            undobuffersize=0
            tracer(0)
            fenetres(ecranquilles,t)
            sleep(0.1)
        résultatschangements=comparerafficherquilles(quilles,quillesavant,len(listequilles[manche])-1)
        for k in résultatschangements:
            xverslequelonva=((randint(45,55)+40*(2*joueur-1))/100-0.5)*window_width()
            yverslequelonva=((20+randint(-5,5))/100-0.5)*window_height()
            print(xverslequelonva,yverslequelonva)
            xactuel,yactuel=listetortuestempquilles[manche][k].pos()
            tortuequisenva=listetortuestempquilles[manche][k]
            tortuequisenva.setheading(tortuequisenva.towards(xverslequelonva,yverslequelonva))
            for _ in range(10):
                tortuequisenva.forward(tortuequisenva.distance(xverslequelonva,yverslequelonva)/10)
                update()
                print(tortuequisenva.distance(xverslequelonva,yverslequelonva))
        quillesavant=quilles.copy()

        joueur=-1*joueur+1                              #on passe la main
        print(afficherquilles(quilles,len(listequilles[manche])))                              #on affiche les 
        if joueur==1:                                   #si c'est au tour du joueur
            a=joueurjoue(quilles,a)                       #on lance la fonction joueurjoue() pour récuperer a, la réponse du joueur
        else:                                           #sinon(tour de l'ordi)
            a=ordijoue(quilles)                         #on lance la fonction ordijoue() pour récuperer a
        quilles=jouer(quilles,a)                        #on lance la fonction jouer()
    if joueur==1:                                       #fin de la boucle: si joueur=1(tour du joueur)
        print("Bravo! Tu as gagné!")                    #alors le joueur a gagné, on le lui dit
        a="Tu as gagné! Bravo!"
    else:                                               #sinon....
        print("Dommage... l'ordi qui joue presque au hasard t'a battu... En fait t'es vraiment nul.")#ben il est nul et on lui fait culpabiliser à mort
        a="Tu as perdu! Dommage..."
