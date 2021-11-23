##    Jeu de Quilles     ##    par Kylian GIRARD et Ilane PELLETIER du groupe G5

from random import *
from turtle import *

def ecran_titre():      #affiche un ecran titre au lancement du jeu
    
    color("black")      
    up()
    goto(0,100)
    down()
    write("Chat-Boule Tout!",move=False,align="center",font=("Arial",40,"bold","underline"))
    up()            #écrit le titre en grand
    goto(0,0)
    down()
    write("Les chats ne sont ils pas des manipulateurs, avec leur petits yeux et leur corpulence de peluche ?",move=False,align="center",font=("Arial",12,"normal"))
    up()
    goto(0,-100)     #texte d'introduction
    down()
    write("Dans un décor de vielle maison, lancez leur des pelotes de laines pour faire tomber ces démoniaque félins.",move=False,align="center",font=("Arial",12,"normal"))
    up()
    goto(0,-150)
    down()
    write("Passez en plein écran!",move=False,align="center",font=("Arial",12,"normal"))
    up()
    goto(-250,-250)             #cadre de la fausse barre de chargement
    down()
    forward(500)
    left(90)
    forward(100)
    left(90)
    forward(500)
    left(90)
    forward(100)
    left(90)
    color("black","green")
    for i in range (50):        # fause barre de chargement pour laisser le temps de lire et de passer en plein écran
        begin_fill()
        forward(i*10)
        left(90)
        forward(100)
        left(90)
        forward(i*10)
        left(90)
        forward(100)
        left(90)
        end_fill()
    clear()

####
       
def dessinFond():       #dessine le décor du jeu(maison)

    up()
    goto(-largeur/2,-hauteur/2)     #dessine le cadre du décor de la fenêtre
    down()
    color("black")
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)


    up()                                #dessine le sol de la pièce
    goto(-largeur/2,-hauteur/2)
    down()
    color("black", "saddlebrown")
    begin_fill()
    goto(largeur/2,-hauteur/2)
    goto(largeur/4,-hauteur/4)
    goto(-largeur/4,-hauteur/4)
    goto(-largeur/2,-hauteur/2)
    end_fill()

    color("black","brown")          #dessine le mur de gauche
    begin_fill()
    goto(-largeur/4,-hauteur/4)
    goto(-largeur/4,hauteur/2)
    goto(-largeur/2,hauteur/2)
    goto(-largeur/2,-hauteur/2)
    end_fill()

    goto(largeur/2,-hauteur/2)  #dessine le mur de droite
    begin_fill()
    goto(largeur/2,hauteur/2)
    goto(largeur/4,hauteur/2)
    goto(largeur/4,-hauteur/4)
    goto(largeur/2,-hauteur/2)
    end_fill()
    

    color("black","maroon")         #dessine le mur du fond
    up()
    goto(largeur/4,hauteur/2)
    begin_fill()
    down()
    goto(-largeur/4,hauteur/2)
    goto(-largeur/4,-hauteur/4)
    goto(largeur/4,-hauteur/4)
    end_fill()

    up()                            #dessine le cadre de la fenêtre
    goto(-hauteur/30,-hauteur/30)
    down()
    setheading(0)
    color("black","grey")
    begin_fill()
    for i in range (4):
        forward(hauteur/4 +hauteur/15)
        left(90)
    end_fill()

    up()                            #dessine le trou de la fenêtre
    goto(0,0)
    down()
    color("black","royalblue")
    begin_fill()
    for i in range (4):
        forward(hauteur/4)
        left(90)
    end_fill()
    
    color("black","grey")       #dessine le cadre interieur de la fenêtre
    forward(hauteur/8 -hauteur/120)
    left(90)
    begin_fill()
    forward(hauteur/4)
    up()
    goto(hauteur/8 +hauteur/120, ycor())
    setheading(-90)
    forward(hauteur/4)
    end_fill()
    up()
    goto(0,hauteur/8 +hauteur/120)
    down()
    begin_fill()
    setheading(0)
    forward(hauteur/4)
    up()
    goto(hauteur/4,hauteur/8 -hauteur/120)
    down()
    setheading(180)
    forward(hauteur/4)
    end_fill()
    up()

    goto(0,-hauteur/2)      #affiche une pelotte de laine au bas de la fenêtre de jeu
    down()
    setheading(0)
    pelote(150)
    up()
    

####

def afficheQuilles(q,n):        #affiche les différentes quilles (debouts et couchées)

    dessinFond()
    
    r=""        #liste à afficher
    j=0         #numéro de la sous liste

    if q==[]:

        for i in range (n):

            dessinChatCouché(i,j) #on affiche uniquement des quilles couchées (car la liste de quilles debouts est vide)
    else:                
        for i in range (n):     #parcours toutes les quilles

            if( i> max(q[j])and j<len(q)-1):        #si la quille n'est pas dans la sous liste et que ce n'était pas la dernière

                color("green")
                up()
                goto(xcor()- (i - q[j][0])*40, ycor()-30)   #affiche le numéro de la ligne
                down()
                begin_fill()
                forward(20)
                left(90)
                forward(20)
                left(90)
                forward(20)
                left(90)
                forward(20)
                left(90)
                end_fill()
                color("black")
                up()
                goto(xcor()+7,ycor()+3)
                down()
                write(j+1)
                
                j+=1    #on passe à la liste suivante

            if( i >= min(q[j]) and i<= max(q[j])):  #si i est dans la liste 
                dessinChatDebout(i,j)      #on affiche un chat debout
                

            else:           

                 dessinChatCouché(i,j)     #sinon on affiche un chat couché
                 up()
                 goto(xcor()+30,ycor())
                 down()
                 pelote(40)
                 up()
                 goto(xcor()-30,ycor())
                 down()

        color("green")
        up()
        goto(xcor()- (i-max(q[j]))*80-(max(q[j])-min(q[j]))*40, ycor()-30)  #affiche le numéro de la dernière ligne
        down()
        begin_fill()
        setheading(0)
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(20)
        left(90)
        end_fill()
        color("black")
        up()
        goto(xcor()+7,ycor()+3)
        down()
        write(j+1)


#####

def coussinet():
    r=50
    color ("black")         #dessine une empreinte de chat 
    down()
    begin_fill()
    circle(r)
    end_fill()
    up()
    right(300)
    forward(r*2.5)
    down()
    begin_fill()
    circle(r/3)
    end_fill()
    up()
    right(-80)
    forward(r*1.3)
    down()
    begin_fill()
    circle(r/3)
    end_fill()
    up()
    right(-55)
    forward(r*1.3)
    down()
    begin_fill()
    circle(r/3)
    end_fill()

####

def dessinChatDebout(i,j):

    x= -largeur/4 -largeur/16 + (i)*80
    y= -hauteur/3
    up()
    goto(x,y)
    setheading(0)
    down()
    rad=40          #taille du corps du chat

    color("black","grey")       #corps
    begin_fill()
    circle(rad)
    end_fill()

    up()                        #tête 
    goto(xcor(),ycor()+2*rad -5)
    down()
    begin_fill()
    circle(rad/2)
    end_fill()

    up()
    goto(xcor()-rad/5,ycor()+rad/3) #oeil gauche
    down()
    color("black","white")
    begin_fill()
    circle(rad/6)
    end_fill()
    color("black")
    
    
    up()
    goto(xcor()+rad/24, ycor()+rad/24)  #pupille oeil gauche
    down()
    begin_fill()
    circle(rad/9)
    end_fill()
    up()
    goto(xcor()-rad/24, ycor() - rad/24)
    down()

    up()
    goto(xcor()+rad/2.5,ycor()) #oeil droit
    down()
    color("black","white")
    begin_fill()
    circle(rad/6)
    end_fill()
    color("black")

    up()
    goto(xcor()-rad/24, ycor()+rad/24)  #pupille oeil droit
    down()
    begin_fill()
    circle(rad/9)
    end_fill()
    up()
    goto(xcor()+rad/24, ycor() - rad/24)
    down()

    up()
    goto(xcor()-rad/3.5, ycor())        #museau
    down()
    color("pink")
    begin_fill()
    goto(xcor()+rad/6, ycor())
    goto(xcor()-rad/12, ycor()-rad/12)
    goto(xcor()-rad/12, ycor()+rad/12)
    end_fill()

    goto(xcor()+rad/12, ycor()-rad/12)  #babines
    color("black")
    setheading(90)
    circle(rad/12, -180)
    circle(rad/12,180)
    setheading(-90)
    circle(rad/12,180)
    circle(rad/12,-180)


    up()
    goto(xcor()+rad/10,ycor()+rad/48)   #moustaches droite
    down()
    goto(xcor()+rad/3, ycor()+rad/18)
    goto(xcor()-rad/3, ycor()-rad/18)
    goto(xcor()+rad/3, ycor()-rad/18)
    goto(xcor()-rad/3, ycor()+rad/18)
    goto(xcor()+rad/3, ycor()-rad/6)
    goto(xcor()-rad/3, ycor()+rad/6)

    up()
    goto(xcor()-rad/5,ycor())       #moustaches gauche
    down()
    goto(xcor()-rad/3, ycor()+rad/18)
    goto(xcor()+rad/3, ycor()-rad/18)
    goto(xcor()-rad/3, ycor()-rad/18)
    goto(xcor()+rad/3, ycor()+rad/18)
    goto(xcor()-rad/3, ycor()-rad/6)
    goto(xcor()+rad/3, ycor()+rad/6)
    up()
    goto(xcor()+rad/10, ycor()-rad/48)
    down()

    
    up()
    goto(xcor()- rad/2.3, ycor()+rad/2.1) #oreille gauche
    down()
    color("black","grey")
    begin_fill()
    goto(xcor()+rad/4,ycor()+rad/4)
    goto(xcor()-rad/3,ycor()+rad/6)
    goto(xcor()+rad/12, ycor()-5*rad/12)
    end_fill()

    up()
    goto(xcor()+ 2*rad/2.3 , ycor())    #oreille droite
    down()
    color("black","grey")
    begin_fill()
    goto(xcor()-rad/4,ycor()+rad/4)
    goto(xcor()+rad/3,ycor()+rad/6)
    goto(xcor()-rad/12, ycor()-5*rad/12)
    end_fill()

    up()
    goto(xcor()-rad/2.3, ycor()-rad/2.1)    #pattes avant
    goto(xcor(),ycor()-rad/1.2)
    goto(xcor()-rad/3,ycor())
    down()
    setheading(0)
    circle(rad/6)
    up()
    goto(xcor()+rad/1.5,ycor())
    down()
    circle(rad/6)

    up()
    goto(xcor()-rad/3,ycor())       #pattes arrières
    goto(xcor(),ycor()-1.5*rad)
    goto(xcor()-rad/2,ycor())
    down()
    begin_fill()
    circle(rad/6)
    end_fill()
    up()
    goto(xcor()+rad,ycor())
    down()
    begin_fill()
    circle(rad/6)
    end_fill()

####
def dessinChatCouché(i,j):

    x= -largeur/4 -largeur/16 + (i)*80
    y= -hauteur/3
    up()
    goto(x,y)
    setheading(0)
    down()
    rad=40          #taille du corps du chat

    color("black","grey")       #corps
    begin_fill()
    circle(rad)
    end_fill()

    up()                        #tête 
    goto(xcor(),ycor())
    down()
    color("black","grey")
    begin_fill()
    circle(rad/2)
    end_fill()
    
    up()
    goto(xcor()-rad/5,ycor()+rad/3) #oeil gauche
    color("black")
    up()
    circle(rad/6,90)
    down()
    circle(rad/6,180)
    up()
    circle(rad/6,90)
    color("black")


    up()
    goto(xcor()+rad/2.5,ycor()) #oeil droit
    color("black")
    circle(rad/6)
    up()
    circle(rad/6,90)
    down()
    circle(rad/6,180)
    up()
    circle(rad/6,90)
    
    color("black")

    up()
    goto(xcor()-rad/3.5, ycor())        #museau
    down()
    color("pink")
    begin_fill()
    goto(xcor()+rad/6, ycor())
    goto(xcor()-rad/12, ycor()-rad/12)
    goto(xcor()-rad/12, ycor()+rad/12)
    end_fill()

    goto(xcor()+rad/12, ycor()-rad/12)  #babines
    color("black")
    setheading(90)
    circle(rad/12, -180)
    circle(rad/12,180)
    setheading(-90)
    circle(rad/12,180)
    circle(rad/12,-180)


    up()
    goto(xcor()+rad/10,ycor()+rad/48)   #moustaches droite
    down()
    goto(xcor()+rad/3, ycor()+rad/18)
    goto(xcor()-rad/3, ycor()-rad/18)
    goto(xcor()+rad/3, ycor()-rad/18)
    goto(xcor()-rad/3, ycor()+rad/18)
    goto(xcor()+rad/3, ycor()-rad/6)
    goto(xcor()-rad/3, ycor()+rad/6)

    up()
    goto(xcor()-rad/5,ycor())       #moustaches gauche
    down()
    goto(xcor()-rad/3, ycor()+rad/18)
    goto(xcor()+rad/3, ycor()-rad/18)
    goto(xcor()-rad/3, ycor()-rad/18)
    goto(xcor()+rad/3, ycor()+rad/18)
    goto(xcor()-rad/3, ycor()-rad/6)
    goto(xcor()+rad/3, ycor()+rad/6)
    up()
    goto(xcor()+rad/10, ycor()-rad/48)
    down()

    
    up()
    goto(xcor()- rad/2.3, ycor()+rad/2.1) #oreille gauche
    down()
    color("black","grey")
    begin_fill()
    goto(xcor()+rad/4,ycor()+rad/4)
    goto(xcor()-rad/3,ycor()+rad/6)
    goto(xcor()+rad/12, ycor()-5*rad/12)
    end_fill()

    up()
    goto(xcor()+ 2*rad/2.3 , ycor())	#oreille droite
    down()
    color("black","grey")
    begin_fill()
    goto(xcor()-rad/4,ycor()+rad/4)
    goto(xcor()+rad/3,ycor()+rad/6)
    goto(xcor()-rad/12, ycor()-5*rad/12)
    end_fill()
    
    up()
    goto(xcor()+rad/5 , ycor()-rad/2.2)	#patoune droite
    down()
    color("black","grey")
    begin_fill()
    circle(rad/6)
    end_fill()
    
    up()
    goto(xcor()-rad*1.6 , ycor())         #patoune gauche
    down()
    color("black","grey")
    begin_fill()
    circle(rad/6)
    end_fill()
    
    up()
    goto(xcor()+rad*0.9,ycor()+rad*1.9) #queue
    circle(rad/3,90)
    down()
    color("grey","grey")
    begin_fill()
    circle(rad/3,180)
    circle(rad/10,180)
    left(180)
    circle(rad/6,-180 )
    end_fill()
    up()
    goto(xcor(),ycor()-rad*2)
    down()

####
    
def pelote(r):                 #dessine une pelote
    up()
    rayon=r
    color("black","pink")
    down()
    begin_fill()
    circle(rayon/3)
    end_fill()
    circle(rayon/3,10)
    left(30)
    circle(rayon/3,150)
    left(50)
    circle(rayon/3,100)
    color("black","pink")
    begin_fill()
    forward(rayon/2)
    left(90)
    forward(rayon/50)
    left(90)
    forward(rayon/2)
    end_fill()

####

def jouerMilieu(c,q):       #supprime les quilles correspondantes à un tir au milieu d'unne ligne

    i=c[0]      #numéro de la ligne

    if (max(q[i])-min(q[i]) >=3):
    
        moitie=int(min(q[i])+(max(q[i])-min(q[i]))/2)    #valeur du milieu de cette ligne

        q.insert(i+1,[moitie+2,max(q[i])])      #rajoute la deuxième moitié de liste à la suite de la liste coupée
        q.insert(i+1,[q[i][0],moitie-1])        #rajoute la première moitié de la liste à la suite de la liste coupée

        q.remove(q[i])          #supprime la liste coupée

        

    elif max(q[i])-min(q[i]) == 2:  #si il reste 3 quilles dans la ligne

        del q[i][0]     #on garde que la quille de droite

    else:       #si il y a 2 quilles dans la ligne

        del q[i]    #on supprime la ligne

    

###

def jouerCote(c,q):     #supprime les quilles correspondantes à un tir sur un côté d'une ligne

    i=c[0]      #nombre de lignes 

    if (max(q[i])-min(q[i]) >=2):   #si il y a 3 quilles ou plus dans la ligne

        if (c[1]=="G" or c[1] =="g"):               #si on joue à gauche

            q[i].insert(1,(q[i][0]+1))  #
            del q[i][0]                 #on retire la quille de gauche de la liste
        

        if (c[1]=="D" or c[1] =="d"):               #si on joue à droite

            q[i].append((q[i][1]-1))    #
            del q[i][1]                 #on retire la quilles de droite de la liste

    elif max(q[i])-min(q[i])==1:        #si la liste contient 2 quilles

        if (c[1]=="G" or c[1] =="g"):       #si on joue à gauche
            del q[i][0]     #on supprime la première quille de la liste

        if (c[1]=="D" or c[1] =="d"):       #si on joue à droite
            del q[i][1]     #on supprime la dernière quille de la liste

    else:       #si il n'y a qu'une quille dans la liste
        
        del q[i]    #on supprime la liste

    

####

def JoueurJoue(q):      #récupère le choix du joueur(ligne et direction)

    i= int(textinput("ligne","Sur quelle ligne voulez vous jouer?(numéro en vert)"))    #demande la ligne sur laquelle le joueur veux jouer
    p= textinput("direction","voulez vous jouer à gauche, au milieu ou a droite de cette ligne?(G, M, ou D)") #demande la direction du tir du joueur
    
    if(i >=0 and i <= len(q)):      #Si la ligne existe

        i-=1            #on transforme le numéro de la ligne en sa place dans q
        c=[i,p]         #on récupère les choix du joueur
        
        if (c[1]=="M" or c[1]=="m"):       #si on joue au milieu
            jouerMilieu(c,q)
        elif ( c[1] == "G" or c[1] =="g" or c[1]=="D" or c[1] =="d"):               #si on joue sur les côtés
            jouerCote(c,q)
        else:           #si la direction indiquée n'existe pas
            textinput("erreur","Votre direction n'existe pas, c'est au tour de l'ordinateur")
    else:               #si la liste existe pas
        textinput("erreur","Votre ligne n'existe pas, c'est au tour de l'ordinateur")

####

def ordiJoue(q):        #permet à l'ordinateur de jouer

    i= randint(0,(len(q)-1))    #l'ordinateur choisi une liste aléatoire
    p= choice(['G','M','D'])    #l'ordinateur choisi une direction aléatoire

    c=[i,p]     #on récupère les choix de l'ordi

    if c[1]=="M":       #si l'ordi joue au milieu
        jouerMilieu(c,q)
    else:               #i l'ordi joue sur les côtés
        jouerCote(c,q)

####

screensize(1920,1080)   #taille de la fenêtre 
speed(0)                #vitesse de dessin
ht()                    #on cache la flêche de dessin

hauteur = 800         #taille du fond d'écran
largeur = 2000

ecran_titre()           #on execute la procédure affichant l'ecran de démarrage
speed(0)

nInit= randint(12,16)        #nombre de quilles de départ aléatoire
n=nInit
q=[[0,n-1]]                 #liste des lignes de quilles

tracer(0)
afficheQuilles(q,n)         #affiche les quilles
update()

while q != []:      #tant qu'il reste des quilles

    JoueurJoue(q)       #le joueur joue
    
    tracer(0)
    afficheQuilles(q,n) #on affiche les quilles restantes
    update()

    
    if( q== []):    #si il ne reste plus de quilles
        
        clearscreen()           #affiche l'écran de victoire
        speed(0)
        ht()
        up()
        goto(xcor()-400,ycor())
        write("Bravo! Vous avez gagné!",move=False,align="left",font=("Arial",50,"normal"))
        up()
        goto(-150,200)
        down()
        coussinet()     #dessine l'empreinte de chat
        up()
        goto(400,-300)
        down()
        setheading(0)
        pelote(300)    #dessine une pelote sur l'écran de fin

        re=textinput("rejouer","Voulez vous rejouer? oui/non")  #demande si on veut relancer le jeu
        if re == "oui":
            nInit= randint(10,15)        #nombre de quilles de départ aléatoire
            n=nInit
            q=[[0,n-1]]                 #liste des lignes de quilles
            tracer(0)
            afficheQuilles(q,n)         #affiche les quilles
            update()
            
    else:           #si il reste des quilles
        ordiJoue(q)     #l'ordinateur joue

        afficheQuilles(q,n) #affiche les quilles restantes
        

        if(q==[]):     #si il ne reste plus de quilles
            
            clearscreen()       #affiche l'écran de défaite
            speed(0)
            ht()
            up()
            goto(xcor()-400,ycor())
            write("Dommage! Vous avez perdu!",move=False,align="left",font=("Arial",50,"normal"))

            re=textinput("rejouer","Voulez vous rejouer? oui/non")  #demande si on veut relancer le jeu
            if re == "oui":
                nInit= randint(10,15)        #nombre de quilles de départ aléatoire
                n=nInit
                q=[[0,n-1]]                 #liste des lignes de quilles
                tracer(0)
                afficheQuilles(q,n)         #affiche les quilles
                update()