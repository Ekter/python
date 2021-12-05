#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:41:49 2020

@author: user
"""
import random
import pygame
from pygame.locals import *
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
niveau=[
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
]
x=4
inertie_gauche=0
inertie_droite=0
v=0
test=0
test2=0
test3=0
pygame.init()
fenetre = pygame.display.set_mode((1000,700))
pygame.display.set_caption('Marie le boss')
gravite=2
s1=pygame.image.load("sol1.png").convert()
s2=pygame.image.load("sol2.png").convert()
s3=pygame.image.load("sol3.png").convert()
s4=pygame.image.load("sol4.png").convert()
s5=pygame.image.load("sol5.png").convert()
ciel=pygame.image.load("ciel.png").convert()
perso=pygame.image.load("Perso.png").convert_alpha()
position_perso = perso.get_rect()
collage_du_fond()
musique=pygame.mixer.Sound("musique.wav")
musique.play()
position_perso= position_perso.move(0,-1)
fenetre.blit(perso, position_perso)
pygame.display.flip()
continuer=1
pygame.key.set_repeat(50,20)
clock=pygame.time.Clock()
while continuer:
    clock.tick(60)
    perso_i=int(position_perso.y/35)+2
    perso_j=int(position_perso.x/40)
    touche=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN and touche[K_UP]==1 and test3 == 0:
            if niveau[perso_i][perso_j+1]==4:
                gravite=-gravite
                test3=1
                position_perso= position_perso.move(0,gravite)
        if event.type == KEYDOWN and touche[K_RIGHT]==1:
            if niveau[perso_i-1][perso_j]==0:
                    x=x+0.4
                    v=10-(40/x)
                    if v<3:
                        v=3
                    position_perso= position_perso.move(v,0)
                    test2=1
        elif event.type==KEYUP and test2==1:
            inertie_droite=1
            test2=0
        if event.type == KEYDOWN and touche[K_LEFT]==1:
            if niveau[perso_i-1][perso_j]==0:
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
    if niveau[perso_i][perso_j+1]!=4:
        position_perso= position_perso.move(0,gravite)
    if inertie_droite==1:
        x=x-3
        if x<=4:
            x=4
            inertie_droite=0
        v=10-(40/x)
        pygame.time.delay(20)
        position_perso= position_perso.move(v,0)
    if inertie_gauche==1:
        x=x-3
        if x<=4:
            x=4
            inertie_gauche=0
        v=-(10-(40/x))
        pygame.time.delay(20)
        position_perso= position_perso.move(v,0)
    print("Etat inertie gauche :"+str(inertie_gauche))
    print("Etat inertie droite :"+str(inertie_droite))
    print("Le x vaut : "+str(x))
    print("La vitesse vaut : "+str(v))
    collage_du_fond()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()            
pygame.quit()