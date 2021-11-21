#Jeu du pendu, codé par Nino Mulac
from turtle import *
from random import choice
def afficherbonhomme(listebonhomme):
    for i in listebonhomme:
        if i[0]=="line":
            penup()
            goto(i[1],i[2])
            pendown()
            goto(i[3],i[4])
        if i[0]=="circle":
            left(i[1])
            circle(i[2])

listebonhomme=[["line",-50,0,50,0],["line",0,0,0,300],["line",0,300,100,300],["line",0,250,50,300],["line",100,300,100,250],["circle",180,37],["line",100,176,100,71],["line",100,71,70,20],["line",100,71,130,20],["line",50,140,150,140]]
print("ouverture du fichier")
fichier=open("dicoFrancais.txt","r")
listemots=[ligne.rstrip() for ligne in fichier]
fichier.close()
print("fermeture du fichier")
speed(0)
motadeviner=choice(listemots)
print("choix du mot")