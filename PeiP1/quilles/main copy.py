#Programme créé par Nino Mulac et Hugo Durand, visant à produire une variante du jeu de Nim, pour le projet de programmation impérative
#On part du principe que une quille seule est une liste de la forme [n,n+1], pour que fin-début soit le nombre de quilles de la ligne.
#Importations: turtle pour l'interface graphique, pynnput pour les controles au clavier, time pour les delais, et random pour l'aléatoire
from turtle import *                                #pour l'interface graphique
from pynput.keyboard import Key, Controller         #pour les contrôles au clavier
from time import sleep                              #pour les délais, mais pas encore utilisés
from random import randint, choice, random          #pour l'aléatoire

#fonction afficherquilles : par une liste en compréhension, on parcourt les sous listes de c, et on join les sous-chaines, puis on y ajoute le début et la fin de la ligne de quilles, avec des quilles tombées.
def afficherquilles(c,nlim):
    return "-"*(c[0][0]-1)+"".join(["-"*(c[i][0]-c[i-1][1])+"|"*(c[i][1]-c[i][0])+"-"*(nlim-c[len(c)-1][1]) for i in range(0,len(c))])
#fin

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

#fonction joueurjoue, boucle tant que c'est pas bon
def joueurjoue(q):
    Cpasbon=1                                       #Cpasbon est une variable pour boucler tant que la réponse de l'utilisateur
    while Cpasbon!=0:                               #boucle tant que c'est pas bon
        a=textinput("Jeu des quilles","Où voulez-vous jouer?")#input du choix de jeu
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
        lettresjeu=a[pos+1:]                        #on assigne lettrejeu
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
nlimitquilles=randint(7,13)                         #on choisit aléatoirement le nombre de quilles
quilles=[[1,nlimitquilles]]                         #on crée la liste des quilles
joueur=0                                            #joueur=0:ordi; joueur=1:humain, on alterne au début de la boucle.

while len(quilles)>0:                               #boucle tant qu'il reste des quilles
    joueur=-1*joueur+1                              #on passe la main
    afficherquilles(quilles,nlimitquilles)                              #on affiche les 
    if joueur==1:                                   #si c'est au tour du joueur
        a=joueurjoue(quilles)                       #on lance la fonction joueurjoue() pour récuperer a, la réponse du joueur
    else:                                           #sinon(tour de l'ordi)
        a=ordijoue(quilles)                         #on lance la fonction ordijoue() pour récuperer a
    quilles=jouer(quilles,a)                        #on lance la fonction jouer()
if joueur==1:                                       #fin de la boucle: si joueur=1(tour du joueur)
    print("Bravo! Tu as gagné!")                    #alors le joueur a gagné, on le lui dit
else:                                               #sinon....
    print("Dommage... l'ordi qui joue presque au hasard t'a battu... En fait t'es vraiment nul.")#ben il est nul et on lui fait culpabiliser à mort
