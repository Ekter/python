import time
import math
from turtle import *
from typing import Any, Callable, Dict, List, Optional, Sequence, Text, Tuple, TypeVar, Union, overload

atome = Shape("compound")
fillcolor("#000000")
forward(-10)
begin_poly()
right(90)
circle(10)
end_poly()
atome.addcomponent(get_poly(),(1,0,0) ,(0,0,0))
addshape('atome', shape=atome)



class Atome(object):
    "objet de test"
    def __init__(self,posx=0,posy=0,vitnorme=0,vitdir=0,charge=1,masse=1,taille=1):
        self.posx=posx
        self.posy=posy
        self.vitnorme=vitnorme
        self.vitdir=vitdir
        self.charge=charge
        self.masse=masse
        self.taille=taille
    def bougervitesse(self) ->None:
        self.posx+=self.vitnorme*math.cos(self.vitdir/180*math.pi)
        self.posy+=self.vitnorme*math.sin(self.vitdir/180*math.pi)
    def distance(self,atome) ->float:
        return ((self.posx-atome.posx)**2+(self.posy-atome.posy)**2)**(1/2)
    def appliquergravite(self,atome,g=1) -> None:
        "Cette fonction modifie la vitesse en fonction de l'effet de la gravité dù à un atome sur un autre."
        angleacc=math.atan2(self.posy-atome.posy,self.posx-atome.posx)/math.pi*180
        normeacc=g*self.masse*atome.masse/(self.distance(atome)**2)/self.masse
        self.vitnorme=((self.vitnorme*math.cos(self.vitdir/180*math.pi)+normeacc*math.cos(angleacc/180*math.pi))+(self.vitnorme*math.sin(self.vitdir/180*math.pi)+normeacc*math.sin(angleacc/180*math.pi)))**(1/2)
        """if self.posx<atome.posx:
            self.vitx+=g*(self.masse*atome.masse)/(self.posx-atome.posx)**2/self.masse
        else:
            self.vitx-=g*(self.masse*atome.masse)/(self.posx-atome.posx)**2/self.masse
        if self.posy<atome.posy:
            self.vity+=g*(self.masse*atome.masse)/(self.posy-atome.posy)**2/self.masse
        else:
            self.vity-=g*(self.masse*atome.masse)/(self.posy-atome.posy)**2/self.masse
"""

def afficherlisteatomes(liste: List[Atome]) -> None :
    l=[]
    for i in liste:
        l.append((int(i.posx),int(i.posy)))
        print(i.vitx,i.vity,i.posx,i.posy)
    for k in range(-10,10,1):
        if k in [i[1] for i in l]:
            print(" "*(10+l[[i[1] for i in l].index(k)][0])+"@")
        else:
            print(" "*21)

    #print(l)
def dessinerlisteatomes(liste:List[Atome]) -> None :
    penup()
    clear()
    for i in liste:
        tortue=Turtle("atome")
        tortue.penup()
        tortue.speed(0)
        tortue.turtlesize(i.masse)
        tortue.goto(i.posx,i.posy)
        tortue.stamp()
g=9.81
atome1=Atome(-43,25,1,90,1,10,1)
atome2=Atome(60,30,5,180,5,3,10)
while True:
    dessinerlisteatomes([atome1,atome2])
    time.sleep(1)
    atome1.appliquergravite(atome2)
    atome2.appliquergravite(atome1)
    atome1.bougervitesse()
    atome2.bougervitesse()
    print(atome1.posx,atome1.posy,atome2.posx,atome2.posy)
