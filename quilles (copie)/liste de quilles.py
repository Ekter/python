from turtle import *
quilles=[[0,10],[13,15]]
def printquilles(quilles):
    for i in range (0,quilles[0][0]):
        print("_")
    for pointeur in range(len(quilles)):
        if pointeur>0:
            for i in range(quilles[pointeur-1][1],quilles[pointeur][0]):
                print("_",end="")
        for k in range(quilles[pointeur][0],quilles[pointeur][1]):
            print("|",end="")

while len(quilles)>0:
    a=textinput("Jeu des quilles","Où voulez-vous jouer?")
    nlignejeu=int(a[:a.find(":")])
    printquilles(quilles)
