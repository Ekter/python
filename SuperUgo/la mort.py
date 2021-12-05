#0!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:09:55 2020

@author: user
"""

import pygame, pygame.font, pygame.event, pygame.draw, string
import random
from pygame.locals import *
def quel_niveau(num): #13 colonnes 14 lignes
   if num==1:      
       niveau=[[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,9,9,0,0,9,9,9,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,9,9,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,9,9,0,0,0,0,2,2,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50]]
   elif num==2:
       niveau=[[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,9,9,9,9,9,9,9,9,9,9,9,9,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,9,50],
               [0,0,0,0,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,9,50],
               [0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,9,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,9,50],
               [0,0,0,9,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,9,50],
               [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50]]
   elif num==3:
       niveau=[[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,9,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,9,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,9,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,9,0,0,0,0,2,0,0,0,0,0,0,9,0,0,0,0,50],
               [0,0,0,0,0,0,0,9,2,0,0,0,0,2,0,0,0,0,0,0,0,9,0,0,0,50],
               [0,0,0,0,0,0,9,2,2,0,0,0,0,2,0,0,0,0,0,0,0,0,9,0,0,50],
               [0,0,0,0,0,9,2,2,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,9,2,2,2,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,2,2,2,2,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,50],
               [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50]]
   elif num==4:
       niveau=[[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50]]
   elif num==5:
       niveau=[[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50]]
   return niveau
def display_text(message,x_box,y_box,taille,R1,G1,B1):
   global fenetre
   font = pygame.font.Font(None, taille)
   text = font.render(message, 1, (R1, G1,B1))
   textpos = text.get_rect(x=x_box,y=y_box)
   fenetre.blit(text, textpos)
def collage_du_fond():
   ligne=0
   while ligne < 20:
       colonne=0
       while colonne < 25:
           if niveau[ligne][colonne]==1:
               fenetre.blit(mur,(colonne*40,ligne*35))
           if niveau[ligne][colonne]==2:
               fenetre.blit(brique,(colonne*40,ligne*35))
           if niveau[ligne][colonne]==4:
               fenetre.blit(sol,(colonne*40,ligne*35))
           if niveau[ligne][colonne]==5:
               fenetre.blit(ciel,(colonne*40,ligne*35))
           if niveau[ligne][colonne]==9:
               fenetre.blit(piece,(colonne*40,ligne*35))
           colonne=colonne+1
       ligne=ligne+1
compteur=0
score=0
anim_saut=0
bouton_gauche_appuyé=0
bouton_droit_appuyé=0
bouton_haut_appuyé=0
double_saut=0
mur_droite=1
mur_gauche=1
gravitation=0
x=4
niv=1
BOUCLE=1
menu=1
scene=0
inertie_gauche=0
inertie_droite=0
v=0
saut_lancé=0
gravite=2
continuer=1
pygame.init()
fenetre = pygame.display.set_mode((1000,700))
pygame.display.set_caption('NewSuperUgo')
sol=pygame.image.load("Sol.png").convert()
ciel=pygame.image.load("Ciel.png").convert()
detect=pygame.image.load("ROUGE.png").convert()
detect2=pygame.image.load("BLEU.png").convert()
panda=pygame.image.load("Panda.png").convert_alpha()
saut1=pygame.image.load("saut1.png").convert_alpha()
saut2=pygame.image.load("saut2.png").convert_alpha()
saut3=pygame.image.load("saut3.png").convert_alpha()
brique=pygame.image.load("brique.png").convert()
mur=pygame.image.load("mur.png").convert()
monstre=pygame.image.load("montre.jpg").convert()
piece=pygame.image.load("piece.png").convert_alpha()
niveau=quel_niveau(niv)
position_panda = panda.get_rect()
collage_du_fond()
position_panda=position_panda.move(0,455)
fenetre.blit(panda,position_panda)
clock = pygame.time.Clock()
while BOUCLE: 
   dt = clock.tick(60)
   for event in pygame.event.get():
       #Quitter
       if event.type == QUIT or event.type == KEYDOWN and event.key ==K_ESCAPE :
           BOUCLE= 0
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
                   BOUCLE=0
               if event.key == K_KP2:
                   menu=0
                   scene=2
               if event.key == K_KP3 :
                   BOUCLE= 0
                   continuer=0
       elif scene == 2 :
           fond2 = pygame.image.load("fondForet.jpg").convert()
           fenetre.blit(fond2, (0,0))
           pygame.display.flip()
clock=pygame.time.Clock()
pygame.key.set_repeat(5,20)
#musique_jeu=pygame.mixer.Sound("Musique_geniale.wav")
#musique_jeu.play()
while continuer:
   clock.tick(60)
   gravitation=0
   ligne_panda=int(position_panda.y/35)+2
   colonne_panda=int(position_panda.x/40)
   touche=pygame.key.get_pressed()
   for event in pygame.event.get():
       pygame.event.pump()
       if event.type == KEYDOWN and touche[K_UP]==1 and saut_lancé == 0 :
           if niveau[ligne_panda][colonne_panda]!=0 or niveau[ligne_panda][colonne_panda+1]!=0:
               gravite=-gravite
               saut_lancé=1
               bouton_haut_appuyé=1
               position_panda= position_panda.move(0,-3)
       elif event.type==KEYUP and bouton_haut_appuyé==1:
           bouton_haut_appuyé=0
           double_saut=1
       if event.type == KEYDOWN and event.key==K_UP  and double_saut == 1:
           saut_lancé=10
           double_saut=0
           anim_saut=1
           if 0  < gravite:
               gravite=-gravite
       if event.type == KEYDOWN and touche[K_RIGHT]==1 and mur_droite==1:
                   x=x+0.4
                   v=10-(40/x)
                   if v<3:
                       v=3
                   position_panda=position_panda.move(v,0)
                   bouton_droit_appuyé=1
                   inertie_droite=0
                   inertie_gauche=0
       elif event.type==KEYUP and bouton_droit_appuyé==1:
           inertie_droite=1
           bouton_droit_appuyé=0
       if event.type == KEYDOWN and touche[K_LEFT]==1 and mur_gauche==1:
                   x=x+0.4
                   v=(10-(40/x))*-1
                   if v>-3:
                       v=-3
                   position_panda=position_panda.move(v,0)
                   bouton_gauche_appuyé=1
                   inertie_gauche=0
                   inertie_droite=0
       elif event.type==KEYUP and bouton_gauche_appuyé==1:
           inertie_gauche=1
           bouton_gauche_appuyé=0
       if event.type == MOUSEMOTION and event.buttons[1]==1:
           continuer=0
       if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
           continuer=0
   if gravite < 0:
       saut_lancé=saut_lancé+1
       if saut_lancé >= 46:
           gravite=-gravite
           saut_lancé=0
           double_saut=0
   if niveau[ligne_panda-1][colonne_panda+1]==50:
       niv=niv+1
       niveau=quel_niveau(niv)
       x=4
       position_panda=position_panda.move(colonne_panda*-40,-35*ligne_panda+490)
   if (niveau[ligne_panda][colonne_panda+0]==0 or niveau[ligne_panda][colonne_panda+0]==9) and (niveau[ligne_panda][colonne_panda+1]==0 or niveau[ligne_panda][colonne_panda+1]==9):
       position_panda=position_panda.move(0,gravite)
   if ((niveau[ligne_panda-2][colonne_panda+0]!=0 and niveau[ligne_panda-2][colonne_panda+0]!=9) and (niveau[ligne_panda-1][colonne_panda+0]==0 or niveau[ligne_panda-1][colonne_panda+0]==9)) or (niveau[ligne_panda-2][colonne_panda+1]!=0 and niveau[ligne_panda-2][colonne_panda+1]!=9) and (niveau[ligne_panda-1][colonne_panda+1]==0 or niveau[ligne_panda-1][colonne_panda+1]==9):
     saut_lancé=46
     if gravite >0:
       gravite=-gravite
   if (niveau[ligne_panda-2][colonne_panda-0]!=0 and niveau[ligne_panda-2][colonne_panda-0]!=9 and niveau[ligne_panda-2][colonne_panda-0]!=50) or niveau[ligne_panda-1][colonne_panda-0] !=0 and niveau[ligne_panda-1][colonne_panda-0] !=50 and niveau[ligne_panda-1][colonne_panda-0] !=9:
     x=4
     v=0
     mur_gauche=0
   else:
     mur_gauche=1
   if (niveau[ligne_panda-0][colonne_panda-0] !=0 and niveau[ligne_panda-0][colonne_panda-0] !=9 and niveau[ligne_panda-0][colonne_panda-0] !=50) and (niveau[ligne_panda-0][colonne_panda+1]==0 or niveau[ligne_panda-0][colonne_panda+1]==9 or niveau[ligne_panda-0][colonne_panda+1]==50):
       position_panda=position_panda.move(0,-3)
       ligne_panda=int(position_panda.y/35)+2
       colonne_panda=int(position_panda.x/40)
       if (niveau[ligne_panda-0][colonne_panda-0] !=0 and niveau[ligne_panda-0][colonne_panda-0] !=50 and niveau[ligne_panda-0][colonne_panda-0] !=9) and (niveau[ligne_panda-0][colonne_panda+1]==0 or niveau[ligne_panda-0][colonne_panda+1]==9 or niveau[ligne_panda-0][colonne_panda+1]==50):
           x=4
           v=0
           mur_gauche=0
       else:
           mur_gauche=1
       position_panda=position_panda.move(0,3)
       ligne_panda=int(position_panda.y/35)+2
       colonne_panda=int(position_panda.x/40)
   if (niveau[ligne_panda-2][colonne_panda+1]!=0 and niveau[ligne_panda-2][colonne_panda+1]!=50 and niveau[ligne_panda-2][colonne_panda+1]!=9) or (niveau[ligne_panda-1][colonne_panda+1]!=0 and niveau[ligne_panda-1][colonne_panda+1]!=50 and niveau[ligne_panda-1][colonne_panda+1]!=9):
     x=4
     v=0
     mur_droite=0
   else:
     mur_droite=1
   if (niveau[ligne_panda-0][colonne_panda+1] !=0 and niveau[ligne_panda-0][colonne_panda+1] !=50 and niveau[ligne_panda-0][colonne_panda+1] !=9) and (niveau[ligne_panda-0][colonne_panda+0]==0 or niveau[ligne_panda-0][colonne_panda+0]==9 or niveau[ligne_panda-0][colonne_panda+0]==50):
       position_panda=position_panda.move(0,-3)
       ligne_panda=int(position_panda.y/35)+2
       colonne_panda=int(position_panda.x/40)
       if (niveau[ligne_panda-0][colonne_panda+1] !=0 and niveau[ligne_panda-0][colonne_panda+1] !=9 and niveau[ligne_panda-0][colonne_panda+1] !=50) and (niveau[ligne_panda-0][colonne_panda+0]==0 or niveau[ligne_panda-0][colonne_panda+0]==9 or niveau[ligne_panda-0][colonne_panda+0]==50):
           x=4
           v=0
           mur_droite=0
       else:
           mur_droite=1
       position_panda=position_panda.move(0,3)
       ligne_panda=int(position_panda.y/35)+2
       colonne_panda=int(position_panda.x/40)
   if inertie_droite==1:
       x=x-3
       if x<=4:
           x=4
           inertie_droite=0
       v=10-(40/x)
       position_panda=position_panda.move(v,0)
   if inertie_gauche==1:
       x=x-3
       if x<=4:
           x=4
           inertie_gauche=0
       v=-(10-(40/x))
       pygame.time.delay(20)
       position_panda=position_panda.move(v,0)
   if niveau[ligne_panda-1][colonne_panda+0]==9:
     score=score+100
     niveau[ligne_panda-1][colonne_panda+0]=0
   if niveau[ligne_panda-2][colonne_panda]==99:    
     score=score+100
     niveau[ligne_panda-2][colonne_panda]=0
   if niveau[ligne_panda-1][colonne_panda+1]==9:
     score=score+100
     niveau[ligne_panda-1][colonne_panda+1]=0
   if niveau[ligne_panda-2][colonne_panda+1]==9:    
     score=score+100
     niveau[ligne_panda-2][colonne_panda+1]=0
   collage_du_fond()
   #display_text("score : " +str(score),0,0,24,0,0,0)
   display_text("score : " +str(score),800,350,24,0,0,0)
   #fenetre.blit(detect,((colonne_panda+0)*40,ligne_panda*35))
   #fenetre.blit(detect2,((colonne_panda+1)*40,ligne_panda*35))
   #fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-3)*35))
   #fenetre.blit(detect,((colonne_panda+0)*40,(ligne_panda-2)*35))
   #fenetre.blit(detect,((colonne_panda+1)*40,(ligne_panda-3)*35))
   #fenetre.blit(detect2,((colonne_panda+1)*40,(ligne_panda-2)*35))
   #fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-2)*35))
   #fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-1)*35))
   #fenetre.blit(detect2,((colonne_panda+0)*40,(ligne_panda-0)*35))
   fenetre.blit(panda,position_panda)
   if anim_saut==1:
       compteur=compteur+1
       if compteur==1:
           x_saut=colonne_panda*40-20
           y_saut=ligne_panda*35
       if compteur <= 5:
           fenetre.blit(saut1,(x_saut,y_saut))
       elif compteur <= 10:
           fenetre.blit(saut2,(x_saut,y_saut))
       elif compteur <= 15:
           fenetre.blit(saut3,(x_saut,y_saut))
       elif compteur ==20:
           compteur=0
           anim_saut=0
   pygame.display.flip()
pygame.quit()