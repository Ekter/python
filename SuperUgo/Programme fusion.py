#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:38:00 2020

@author: user
"""

import pygame, pygame.font, pygame.event, pygame.draw, string
import random
from pygame.locals import *
def quel_niveau(num):
    if num==1:
        niveau=[[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]]
    elif num==2:
        niveau=[[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]]
    return niveau
def display_text(message,x_box,y_box,taille,R1,G1,B1):
    global fenetre
    font = pygame.font.Font(None, taille)
    text = font.render(message, 1, (R1, G1,B1))
    textpos = text.get_rect(x=x_box,y=y_box)
    fenetre.blit(text, textpos)

def collage_du_fond():
    i=0
    while i < 20:
        j=0
        while j < 25:
            if niveau[i][j]==10:
                fenetre.blit(s5,(j*40,i*35))
            if niveau[i][j]==1:
                fenetre.blit(s4,(j*40,i*35))
            if niveau[i][j]==2:
                fenetre.blit(s3,(j*40,i*35))
            if niveau[i][j]==3:
                fenetre.blit(s2,(j*40,i*35))
            if niveau[i][j]==4:
                fenetre.blit(s1,(j*40,i*35))
            if niveau[i][j]==5:
                fenetre.blit(ciel,(j*40,i*35))
            j=j+1
        i=i+1
x=4
a=0
niv=1
continu=1
menu = 1
scene = 0
inertie_gauche=0
inertie_droite=0
v=0
test=0
test2=0
test3=0
gravite=2
continuer=1
pygame.init()
fenetre = pygame.display.set_mode((1000,700))
pygame.display.set_caption('NewSuperUgo')
s1=pygame.image.load("sol1.png").convert()
s2=pygame.image.load("sol2.png").convert()
s3=pygame.image.load("sol3.png").convert()
s4=pygame.image.load("sol4.png").convert()
s5=pygame.image.load("sol5.png").convert()
ciel=pygame.image.load("ciel.png").convert()
detect=pygame.image.load("ROUGE.png").convert()
detect2=pygame.image.load("BLEU.png").convert()
detect3=pygame.image.load("VERT.png").convert()
detect4=pygame.image.load("VIOLET.png").convert()
detect5=pygame.image.load("JAUNE.png").convert()
perso=pygame.image.load("Perso.png").convert_alpha()
niveau=quel_niveau(niv)
position_perso = perso.get_rect()
collage_du_fond()
position_perso= position_perso.move(0,0)
fenetre.blit(perso, position_perso)

clock = pygame.time.Clock()
while continu:
    dt = clock.tick(60)
    for event in pygame.event.get():
        #Quitter
        if event.type == QUIT or event.type == KEYDOWN and event.key ==K_ESCAPE :
            continu = 0
            continuer=0
        if menu == 1:
            fond = pygame.image.load("fondMenu.jpg").convert()
            fenetre.blit(fond, (0,0))
            message1 = "1- Commencer une nouvelle Partie"
            display_text(message1,20,20,32,255,255,255)
            message2 = "2- Reprendre une sauvegarde  "
            display_text(message2,20,60,32,255,255,255)
            message3 = "3- Quitter"
            display_text(message3,20,100,32,255,255,255)
            pygame.display.flip()
            
            if event.type == KEYDOWN:
                if event.key == K_KP1:
                    menu=0
                    continu=0
                if event.key == K_KP2:
                    menu=0
                    scene=2
                if event.key == K_KP3 :
                    continu = 0
                    continuer=0
        elif scene == 2 :
            fond2 = pygame.image.load("fondForet.jpg").convert()
            fenetre.blit(fond2, (0,0))
            pygame.display.flip()
clock=pygame.time.Clock()
pygame.key.set_repeat(1,20)
musique=pygame.mixer.Sound("Musique_geniale.wav")
musique.play()
while continuer:
    clock.tick(60)
    niveau=quel_niveau(niv)
    perso_i=int(position_perso.y/35)+2
    perso_j=int(position_perso.x/40)
    touche=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN and touche[K_UP]==1 and test3 == 0:
            if niveau[perso_i][perso_j+1]==4:
                gravite=-gravite
                test3=1
                position_perso= position_perso.move(0,gravite)
        if event.type == KEYDOWN and touche[K_a]==1:
            niv=1
        elif event.type == KEYDOWN and touche[K_b]==1:
            niv=2
        if event.type == KEYDOWN and touche[K_RIGHT]==1:
                    x=x+0.4
                    v=10-(40/x)
                    if v<3:
                        v=3
                    if niveau[perso_j+1][perso_i-2]!=0:
                        v=0
                    position_perso=position_perso.move(v,0)
                    test2=1
        elif event.type==KEYUP and test2==1:
            inertie_droite=1
            test2=0
        if event.type == KEYDOWN and touche[K_LEFT]==1:
                    x=x+0.4
                    v=(10-(40/x))*-1
                    if v>-3:
                        v=-3
                    position_perso= position_perso.move(v,0)
                    test=1
        elif event.type==KEYUP and test==1:
            inertie_gauche=1
            test=0
        if event.type == MOUSEMOTION and event.buttons[1]==1:
            continuer=0
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer=0
    if gravite < 0:
        test3=test3+1
        if test3 == 40:
            gravite=-gravite
            test3=0
    if niveau[perso_i][perso_j+0]!=4 and niveau[perso_i][perso_j+1]!=4:
        position_perso= position_perso.move(0,gravite)
        if niveau[perso_i][perso_j+0]==4:
            position_perso= position_perso.move(0,-1)
            while niveau[perso_i][perso_j]!=4:
                position_perso= position_perso.move(0,-1)
    if inertie_droite==1:
        x=x-3
        if x<=4:
            x=4
            inertie_droite=0
        v=10-(40/x)
        pygame.time.delay(20)
        if niveau[perso_j+1][perso_i-2]==4:
            v=0
        position_perso= position_perso.move(v,0)
    if inertie_gauche==1:
        x=x-3
        if x<=4:
            x=4
            inertie_gauche=0
        v=-(10-(40/x))
        pygame.time.delay(20)
        if niveau[perso_j][perso_i-2]==4:
            v=0
        position_perso= position_perso.move(v,0)
    #if v < 0:
     #   if niveau[perso_j][perso_i-2]==4:
      #      v=0
    #if 0 < v:
     #   if niveau[perso_j+1][perso_i-2]==4:
      #      v=0
    print("Etat inertie gauche :"+str(inertie_gauche))
    print("Etat inertie droite :"+str(inertie_droite))
    print("Le x vaut : "+str(x))
    print("La vitesse vaut : "+str(v))
    collage_du_fond()
    fenetre.blit(detect,((perso_j+0)*40,perso_i*35))
    fenetre.blit(detect2,((perso_j+1)*40,perso_i*35))
    fenetre.blit(detect3,((perso_j+1)*40,(perso_i-2)*35))
    fenetre.blit(detect4,((perso_j+0)*40,(perso_i-2)*35))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
pygame.quit()