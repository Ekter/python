from time import time

t_timeeee=time()
from random import randint
from typing import Union
import math
import cv2 as cv
import numpy as np

from images2D import Coord2,Triangle2
from image import Image
print(f"imports: {time()-t_timeeee:.4f}s")
t_timeeee=time()

class Coord3():
    def __init__(self, abs, ord, hei) -> None:
        self.abs = abs
        self.ord = ord
        self.hei = hei

    def __repr__(self) -> str:
        return f"({self.abs},{self.ord},{self.hei})"

    def __eq__(self, __o: "Coord3") -> bool:
        return self.abs == __o.abs and self.ord == __o.abs and self.hei == __o.hei

    def __ne__(self, __o: "Coord3") -> bool:
        return not(self == __o)

    def __len__(self):
        return math.sqrt(self.abs**2+self.ord**2+self.hei**2)

    def __add__(self, __o: "Coord3") -> "Coord3":
        return Coord3(self.abs+__o.abs, self.ord+__o.ord, self.hei+__o.hei)

    def __neg__(self) -> "Coord3":
        return Coord3(-self.abs, -self.ord, -self.hei)

    def __sub__(self, __o: "Coord3") -> "Coord3":
        return Coord3(self.abs-__o.abs, self.ord-__o.ord, self.hei-__o.hei)

    def __mul__(self, k: float) -> "Coord3":
        return Coord3(self.abs*k, self.ord*k, self.hei*k)
    
    def replace(self, __o: "Coord3") -> None:
        self.abs = __o.abs
        self.ord = __o.ord
        self.hei = __o.hei
    
    def new(self, abs, ord, hei) -> None:
        self.abs = abs
        self.ord = ord
        self.hei = hei

print(f"Coord3: {time()-t_timeeee:.4f}s")
t_timeeee=time()

class Triangle3():
    def __init__(self, point1: Coord3, point2: Coord3, point3: Coord3):
        self.point1 = point1
        print(f"point1:is self...{point1 is self.point1}")
        self.point2 = point2
        self.point3 = point3

    def __repr__(self) -> str:
        return "Triangle[" + str(self.point1) + "," + str(self.point2) + "," + str(self.point3) + "]"

    def __eq__(self, other: "Triangle3") -> bool:
        return (
            self.point1 == other.point1
            and self.point2 == other.point2
            and self.point3 == other.point3
            if isinstance(other, Triangle3)
            else False
        )

    def __ne__(self, other: "Triangle3") -> bool:
        return not self == other

    def __add__(self, other: "Triangle3"):
        if isinstance(other, Triangle3):
            return Triangle3(
                self.point1 + other.point1,
                self.point2 + other.point2,
                self.point3 + other.point3,
            )
        return Triangle3(self.point1 + other, self.point2 + other, self.point3 + other)

    def __neg__(self):
        return Triangle3(-self.point1, -self.point2, -self.point3)

    def __mul__(self, other: float):
        return Triangle3(self.point1 * other, self.point2 * other, self.point3 * other)

    def __sub__(self, other: "Triangle3"):
        if isinstance(other, Triangle3):
            return Triangle3(self.point1 - other.point1, self.point2 - other.point2, self.point3 - other.point3)
        return Triangle3(self.point1 - other, self.point2 - other, self.point3 - other)

print(f"Triangle3: {time()-t_timeeee:.4f}s")
t_timeeee=time()

class Plan():
    PREC=1
    def __init__(self, x, y, z, const) -> None:
        self.relation = lambda c: c.abs*x+c.ord*y+c.hei*z+const#=0
        #    => x=(hei*z+ord*y+const)/abs
        #    => y=(abs*x+hei*z+const)/ord
        #    => z=(abs*x+ord*y+const)/hei
        self.point=Coord3(x,y,z)
        self.cst=const
        self.project=lambda c: Coord2(10*c.abs+0*c.ord+5*c.hei+50,10*c.ord+10*c.hei+50) #example

    def __contains__(self,c:Union[Coord3,Coord2]):
        return abs(self.relation(c))<=Plan.PREC if type(c) is Coord3 else abs(self.relation(Coord3(c.abs,c.ord,0)))<=Plan.PREC

    def project_Coord3(self,c:Coord3) -> Coord2:
        return self.project(c)

    def project_Triangle3(self,t:Triangle3) -> Triangle2:
        return Triangle2(self.project(t.point1),self.project(t.point2),self.project(t.point3))

print(f"Plan: {time()-t_timeeee:.4f}s")
t_timeeee=time()

if __name__=="__main__":
    print("main: debut")
    p=Plan(1,1,1,0)
    origine=Coord3(0,0,0)
    t3=Triangle3(origine,Coord3(10,0,0),Coord3(0,10,0))
    list_triangles3=[
    Triangle3(Coord3(10,0,0),Coord3(10,10,0), Coord3(0,10,0)),
    Triangle3(origine,Coord3(10,0,0),Coord3(0,10,0)),
    Triangle3(Coord3(10,10,0),Coord3(0,10,0),Coord3(10,10,10)),
    Triangle3(Coord3(0,10,10),Coord3(0,10,0),Coord3(10,10,10)),
    Triangle3(Coord3(0,10,10),Coord3(0,10,0),origine),
    Triangle3(Coord3(0,10,10),Coord3(0,0,10),origine),
    Triangle3(Coord3(0,0,10),Coord3(10,0,0),origine),
    Triangle3(Coord3(0,0,10),Coord3(10,0,0),Coord3(10,0,10)),
    Triangle3(Coord3(10,10,0),Coord3(10,0,0),Coord3(10,0,10)),
    Triangle3(Coord3(10,10,0),Coord3(10,10,10),Coord3(10,0,10)),
    Triangle3(Coord3(10,0,10),Coord3(10,10,10),Coord3(0,0,10)),
    Triangle3(Coord3(0,10,10),Coord3(10,10,10),Coord3(0,0,10)),

    Triangle3(Coord3(22,0,0),Coord3(22,10,0), Coord3(12,10,0)),
    Triangle3(Coord3(12,0,0),Coord3(22,0,0),Coord3(12,10,0)),
    Triangle3(Coord3(22,10,0),Coord3(12,10,0),Coord3(22,10,10)),
    Triangle3(Coord3(12,10,10),Coord3(12,10,0),Coord3(22,10,10)),
    Triangle3(Coord3(12,10,10),Coord3(12,10,0),Coord3(12,0,0)),
    Triangle3(Coord3(12,10,10),Coord3(12,0,10),Coord3(12,0,0)),
    Triangle3(Coord3(12,0,10),Coord3(22,0,0),Coord3(12,0,0)),
    Triangle3(Coord3(12,0,10),Coord3(22,0,0),Coord3(22,0,10)),
    Triangle3(Coord3(22,10,0),Coord3(22,0,0),Coord3(22,0,10)),
    Triangle3(Coord3(22,10,0),Coord3(22,10,10),Coord3(22,0,10)),
    Triangle3(Coord3(22,0,10),Coord3(22,10,10),Coord3(12,0,10)),
    Triangle3(Coord3(12,10,10),Coord3(22,10,10),Coord3(12,0,10)),
    ]
    origine.replace(Coord3(0,0,30))
    print(t3.point1 is origine)
    print(f"main: triangles3:{time()-t_timeeee:.4f}s")
    t_timeeee=time()
    list_triangles2=[p.project_Triangle3(t3) for t3 in list_triangles3]
    print(f"main: triangles2:{time()-t_timeeee:.4f}s")
    t_timeeee=time()
    img=Image(600,400)
    print(f"main: creation img:{time()-t_timeeee:.4f}s")
    tttt=time()
    timeee1=0
    timeee2=0
    timeee3=0
    for t2 in list_triangles2:
        t2.draw_better(img,(255,255,255))
        timeee1+=time()-t_timeeee
        t_timeeee=time()
        t2.draw_points(img)
        timeee2+=time()-t_timeeee
        t_timeeee=time()
        t2.draw_segments(img,col=(0,0,255))
        timeee3+=time()-t_timeeee
        t_timeeee=time()
    print(f"main: draw:{timeee1:.4f}s")
    print(f"main: draw_points:{timeee2:.4f}s")
    print(f"main: draw_segments:{timeee3:.4f}s")
    print(f"main: draw_total:{time()-tttt:.4f}s")
    t_timeeee=time()
    img.to_image("triangle.png")
    print(f"main: write:{time()-t_timeeee:.4f}s")
    print("main: fin")
