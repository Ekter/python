#Projet Roguelike, par Nino Mulac
from time import sleep
import random
from typing import *
from tkinter import *

class Coord(object):
    "Vec2D"
    def __init__(self,x : int =0,y : int =0):
        self.x=int(x)
        self.y=int(y)
    def __repr__(self) -> str:
        return "<"+str(self.x)+","+str(self.y)+">"
    def __eq__(self,other) -> bool:
        return self.x==other.x and self.y==other.y
    def __ne__(self,other) -> bool:
        return not(self==other)
    def __add__(self,other):
        if type(other) is Coord:
            return Coord(self.x+other.x,self.y+other.y)
        if (type(other) is int) or (type(other) is float):
            return Coord(self.x+other,self.y+other)
    def __neg__(self):
        return Coord(-self.x,-self.y)
    def  __mul__(self,other):
        if type(other) is Coord:
            return Coord(self.x*other.x,self.y*other.y)
        if (type(other) is int) or (type(other) is float):
            return Coord(self.x*other,self.y*other)
    def middle(self,other):
        return (self+other)//2
    def __sub__(self,other):
        if type(other) is Coord:
            return Coord(self.x-other.x,self.y-other.y)
        if (type(other) is int) or (type(other) is float):
            return Coord(self.x-other,self.y-other)
    def coin1(self,other):
        return Coord(self.x,other.y)
    def coin2(self,other):
        return Coord(other.x,self.y)
    def __abs__(self):
        return Coord(abs(self.x),abs(self.y))
    def __floordiv__(self,other):
        if type(other) is Coord:
            return Coord(self.x/other.x,self.y/other.y)
        if (type(other) is int) or (type(other) is float):
            return Coord(self.x/other,self.y/other)
    def __truediv__(self,other):
        if type(other) is Coord:
            return Coord(self.x/other.x,self.y/other.y)
        if (type(other) is int) or (type(other) is float):
            return Coord(self.x/other,self.y/other)
    def __len__(self) -> float:
        return (self.x**2+self.y**2)**(1/2)
    def __lt__(self,other):
        if type(other) is Coord:
            return len(self)<len(other)
        if (type(other) is int) or (type(other) is float):
            return len(self)<other
    def __gt__(self,other):
        if type(other) is Coord:
            return len(self)>len(other)
        if (type(other) is int) or (type(other) is float):
            return len(self)>other
    def __le__(self,other):
        if type(other) is Coord:
            return len(self)<=len(other)
        if (type(other) is int) or (type(other) is float):
            return len(self)<=other
    def __ge__(self,other):
        if type(other) is Coord:
            return len(self)>=len(other)
        if (type(other) is int) or (type(other) is float):
            return len(self)>=other


def getch():
    """Single char input, only works only on mac/linux/windows OS terminals"""
    try:
        import termios
        # POSIX system. Create and return a getch that manipulates the tty.
        import sys, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch().decode('utf-8')

class Element(object):
    def __init__(self,name,abbrv=None):
        self.name=name
        if abbrv==None:
            self.abbrv=name[0]
        else:
            self.abbrv=abbrv
    def __repr__(self):
        return self.abbrv
    def description(self):
        return "<{}>".format(self.name)
    def meet(self,hero):
        return Hero.take(hero,self)

class Creature(Element):
    def __init__(self,name,hp,abbrv=None,strength=1):
        Element.__init__(self,name,abbrv)
        self.hp=hp
        self.strength=strength
    def description(self):
        return Element.description(self)+"({})".format(self.hp)
    def meet(self,other):
        self.hp-=other.strength
        if self.hp>0:
            other.hp-=self.strength
            return False
        return True

class Room(object):
    "une salle"
    def __init__(self,c1:Coord,c2:Coord)->None:
        self.c1=c1
        self.c2=c2
    def __contains__(self,coord:Coord)->bool:
        return self.c1.x<=coord.x<=self.c2.x and self.c1.y<=coord.y<=self.c2.y
    def __repr__(self) -> str:
        return f"[<{self.c1.x},{self.c1.y}>, <{self.c2.x},{self.c2.y}>]"
    def center(self)->Coord:
        return self.c1.middle(self.c2)
    def coins(self)->List[Coord]:
        return [self.c1,self.c2,self.c1.coin1(self.c2),self.c2.coin1(self.c1)]
    def intersect(self,other)->bool:
        for i in self.coins():
            if i in other:
                return True
        for i in other.coins():
            if i in self:
                return True
        return False

class Hero(Creature):
    def __init__(self,name="Hero",hp=10,abbrv="@",strength=2):
        Creature.__init__(self,name,hp,abbrv,strength)
        self._inventory=[]
    def take(self,elem):
        self._inventory.append(elem)
        return True
    def description(self):
        return Creature.description(self)+"{}".format(self._inventory)
    def __repr__(self):
        return self.abbrv

class Map(object):
    "carte du jeu"
    ground='.'
    empty=" "
    dir={'z': Coord(0,-1), '\x1b': Coord(0,0) , 's': Coord(0,1), 'd': Coord(1,0), 'q': Coord(-1,0)}
    def __init__(self,size=20,hero=None,ground=".",empty=" ",nbrooms=5,dir={'z': Coord(0,-1), 's': Coord(0,1), 'd': Coord(1,0), 'q': Coord(-1,0)}) -> None:
        self.ground=ground
        self.empty=empty
        self.nbrooms=nbrooms
        self.dir=dir
        self._rooms=[]
        self._roomsToReach=[]
        if hero==None:
            self.hero=Hero()
        else:
            self.hero=hero
        self._mat=[[self.empty for i in range(size)] for k in range(size)]
        self._elem={}
        self.generateRooms(self.nbrooms)
        self.reachAllRooms()
        self.put(self._rooms[0].center(),self.hero)
        self.updatemat()
    def draw(self,fenetre)-> None:
        canvas = Canvas(fenetre)
        for i in range(len(self)):
            for k in range(len(self)):
                if self.get(Coord(i,k))==Map.ground:
                    canvas.create_image(32*k, 32*i, anchor=NE, image= PhotoImage(file = "ground.png"))

        canvas.pack()
    def __repr__(self) -> str:
        return "\n".join(["".join([str(self._mat[k][n]) for k in range(len(self))]) for n in range(len(self))])+"\n"
    def __len__(self) -> int:
        return len(self._mat)
    def __contains__(self,item) -> bool:
        if isinstance(item,Coord):
            return 0<=item.x<=len(self)-1 and 0<=item.y<=len(self)-1
        return item in self._elem.keys()
    def __getitem__(self,item) -> Any:
        if type(item) is Coord:
            return self.get(item)
        else:
            return self.pos(item)
    def __setitem__(self,cle,valeur)->None:
        if type(cle) is Coord:
            self.put(cle,valeur)
        else:
            if not cle in self:
                self.put(valeur,cle)
            else:
                self.tp(cle,valeur)
    def get(self,coord : Coord) -> Element:
        for i,j in self._elem.items():
            if j==coord:
                return i
        return self._mat[coord.y][coord.x]
    def pos(self,element : Element) -> Coord:
        return self._elem.get(element)
    def updatemat(self,x=-1,y=-1,pastouchemap=True) -> None:
        if pastouchemap:
            for i in self._elem.keys():
                    self._mat[self._elem.get(i).x][self._elem.get(i).y]=i.abbrv
        else:
            if x==-1 and y==-1:
                self._mat=[[Map.empty for i in range(len(self._mat))] for k in range(len(self._mat))]
                for i in self._elem.keys():
                    self._mat[self._elem.get(i).x][self._elem.get(i).y]=i.abbrv
            else:
                self._mat[x][y]=Map.ground
                for i in self._elem.keys():
                    self._mat[self._elem.get(i).x][self._elem.get(i).y]=i.abbrv
    def groundize(self,coord : Coord) -> None:
        self._mat[coord.x][coord.y]=Map.ground
    def elementize(self,coord : Coord, abbrv : str) -> None:
        self._mat[coord.x][coord.y]=abbrv
    def put(self,coord : Coord,element : Element) -> None:
        self._elem[element]=Coord(coord.x,coord.y)
        self.elementize(coord,element.abbrv)
    def rm(self,element : Element) -> None:
        if type(element) is Coord:
            self._elem = {key:val for key, val in self._elem.items() if not val == element}
            a=element
        else:
            a=self._elem.pop(element)
        self.groundize(self.pos(a))
    def move(self,element : Element,way : Coord) -> None:
        coordarr=self.pos(element)+way
        if coordarr in self:
            if not coordarr in self._elem.values() and self._mat[coordarr.x][coordarr.y]==Map.ground:
                self.groundize(self.pos(element))
                self._elem[element]=coordarr
                self.elementize(coordarr,element.abbrv)
            elif self._mat[coordarr.x][coordarr.y]!=Map.empty:
                if self.get(coordarr).meet(element):
                    self.rm(coordarr)
    def tp(self,element : Element,dest : Coord) -> None:
        self.move(element,self.pos(element).x-dest.x,self.pos(element).y-dest.y)
    def play(self,fenetre : Tk)-> None:
        print("--- Welcome Hero! ---")
        while self.hero.hp > 0:
            print()
            print(self)
            self.draw(fenetre)
            print(self.hero.description())
            dir= Map.dir.get(getch())
            #self.move(self.hero,  Map.dir[getch()])
            if type(dir) is Coord:
                self.move(self.hero, dir)
        print("--- Game Over ---")
    def remplirrectangle(self,c1:Coord,c2:Coord,thing=" ") -> None:
        for i in range(c1.x,c2.x+1):
            for j in range(c1.y,c2.y+1):
                self._mat[i][j]=thing
    def addRoom(self,room:Room) -> None:
        self._roomsToReach.append(room)
        self.remplirrectangle(room.c1,room.c2,Map.ground)
    def findRoom(self,coord : Coord) -> Any:
        for i in self._roomsToReach:
            if coord in i:
                return i
        return False
    def intersectNone(self,room : Room) -> bool:
        for i in self._roomsToReach:
            if room.intersect(i):
                return False
        return True
    def dig(self,coord : Coord) -> None:
        self._mat[coord.x][coord.y]=Map.ground
        a=self.findRoom(coord)
        if a:
            self._rooms.append(a)
            self._roomsToReach.remove(a)
    def corridor(self,c1 : Coord,c2 : Coord) -> None:
        self.dig(c1)
        coord=Coord(c1.x,c1.y)
        while not(coord==c2):
            coord+=self.dircorridor(coord,c2)
            self.dig(coord)
    def dircorridor(self,c1 : Coord,c2 : Coord) -> Coord:
        if c1.y!=c2.y:
            return Coord(0,1) if c1.y<c2.y else Coord(0,-1)
        if c1.x!=c2.x:
            return Coord(1,0) if c1.x<c2.x else Coord(-1,0)
    def reach(self) -> None:
        r1=random.choice(self._rooms)
        r2=random.choice(self._roomsToReach)
        self.corridor(r1.center(),r2.center())
    def reachAllRooms(self) -> None:
        self._rooms.append(self._roomsToReach.pop(0))
        while len(self._roomsToReach)>0:
            self.reach()
    def randRoom(self) -> Room:
        x1=random.randint(0,len(self)-3)
        y1=random.randint(0,len(self)-3)
        largeur=random.randint(3,8)
        hauteur=random.randint(3,8)
        x2=min(len(self)-1,x1+largeur)
        y2=min(len(self)-1,y1+hauteur)
        return Room(Coord(x1,y1),Coord(x2,y2))
    def generateRooms(self,n) -> None:
        for i in range(n):
            r=self.randRoom()
            if self.intersectNone(r):
                self.addRoom(r)

f=Tk()
m=Map(25)
print(m)
#m.play(f)

"""
██████████
██████████
██████████🍟
██████████0675130307
██████████vignolopatrizia@gmail.com
██████████pattylyra
██████████■
██████████௹₯
█ █ █ █ █
█ █ █ █ █ lgibart@i3s.unice.fr
█ █ █ █ █
"""