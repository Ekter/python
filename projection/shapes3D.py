from images2D import Coord2, Triangle2
from image import Image
import numpy as np
import cv2 as cv
import math
from typing import List, Union
from random import randint
from time import time

t_timeeee = time()

print(f"imports: {time()-t_timeeee:.4f}s")
t_timeeee = time()


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

    @staticmethod
    def randomCoord3(min, max) -> "Coord3":
        return Coord3(randint(min, max), randint(min, max), randint(min, max))


print(f"Coord3: {time()-t_timeeee:.4f}s")
t_timeeee = time()


class Triangle3():
    def __init__(self, point1: Coord3, point2: Coord3, point3: Coord3):
        self.point1 = point1
        # print(f"point1:is self...{point1 is self.point1}")
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
t_timeeee = time()


class Plan():
    PREC = 1

    def __init__(self, x, y, z, const) -> None:
        self.relation = lambda c: c.abs*x+c.ord*y+c.hei*z+const  # =0
        #    => x=(hei*z+ord*y+const)/abs
        #    => y=(abs*x+hei*z+const)/ord
        #    => z=(abs*x+ord*y+const)/hei
        self.point = Coord3(x, y, z)
        self.cst = const
        self.project = lambda c: Coord2(
            1*c.abs+0*c.ord+.5*c.hei+50, 1*c.ord+1*c.hei+50)  # example

    def __contains__(self, c: Union[Coord3, Coord2]):
        return abs(self.relation(c)) <= Plan.PREC if type(c) is Coord3 else abs(self.relation(Coord3(c.abs, c.ord, 0))) <= Plan.PREC

    def project_Coord3(self, c: Coord3) -> Coord2:
        return self.project(c)

    def project_Triangle3(self, t: Triangle3) -> Triangle2:
        return Triangle2(self.project(t.point1), self.project(t.point2), self.project(t.point3))


class Parallelepidedon():
    def __init__(self, point1: Coord3, point2: Coord3) -> None:
        self.point1 = point1
        self.point2 = point2
        self.distx = abs(point1.abs - point2.abs)
        self.disty = abs(point1.ord - point2.ord)
        self.distz = abs(point1.hei - point2.hei)
        self.center = Coord3(
            (point1.abs + point2.abs) / 2, (point1.ord +
                                            point2.ord) / 2, (point1.hei + point2.hei) / 2
        )

        minx = min(point1.abs, point2.abs)
        miny = min(point1.ord, point2.ord)
        minz = min(point1.hei, point2.hei)
        maxx = max(point1.abs, point2.abs)
        maxy = max(point1.ord, point2.ord)
        maxz = max(point1.hei, point2.hei)
        c0 = Coord3(minx, miny, minz)
        c1 = Coord3(maxx, miny, minz)
        c2 = Coord3(minx, maxy, minz)
        c3 = Coord3(minx, miny, maxz)
        c4 = Coord3(maxx, maxy, minz)
        c5 = Coord3(maxx, miny, maxz)
        c6 = Coord3(minx, maxy, maxz)
        c7 = Coord3(maxx, maxy, maxz)

        self.triangles = [
            Triangle3(c1, c4, c2),
            Triangle3(c0, c1, c2),
            Triangle3(c4, c2, c7),
            Triangle3(c6, c2, c7),
            Triangle3(c6, c2, c0),
            Triangle3(c6, c3, c0),
            Triangle3(c3, c1, c0),
            Triangle3(c3, c1, c5),
            Triangle3(c4, c1, c5),
            Triangle3(c4, c7, c5),
            Triangle3(c5, c7, c3),
            Triangle3(c6, c7, c3),
        ]

    def project2(self, plan: Plan) -> List[Triangle2]:
        return [plan.project_Triangle3(t) for t in self.triangles]

    def drawlines(self,img):
        for t in self.project2(Plan(0,0,1,0)):
            t.draw_segments(img, col=(0, 0, 255))

    @staticmethod
    def randomOne():
        return Parallelepidedon(Coord3.randomCoord3(0,200), Coord3.randomCoord3(0,200))



print(f"Plan: {time()-t_timeeee:.4f}s")
t_timeeee = time()

if __name__ == "__main__":
    print("main: debut")
    p = Plan(1, 1, 1, 0)
    c_origin = Coord3(0, 0, 0)
    c1 = Coord3(10, 0, 0)
    c2 = Coord3(0, 10, 0)
    c3 = Coord3(0, 0, 10)
    c4 = Coord3(10, 10, 0)
    c5 = Coord3(10, 0, 10)
    c6 = Coord3(0, 10, 10)
    c7 = Coord3(10, 10, 10)
    dec = Coord3(12, 0, 0)
    t3 = Triangle3(c_origin, c1, c2)
    list_triangles3 = [
        Triangle3(c1, c4, c2),
        Triangle3(c_origin, c1, c2),
        Triangle3(c4, c2, c7),
        Triangle3(c6, c2, c7),
        Triangle3(c6, c2, c_origin),
        Triangle3(c6, c3, c_origin),
        Triangle3(c3, c1, c_origin),
        Triangle3(c3, c1, c5),
        Triangle3(c4, c1, c5),
        Triangle3(c4, c7, c5),
        Triangle3(c5, c7, c3),
        Triangle3(c6, c7, c3),

        Triangle3(c1+dec, c4+dec, c2+dec),
        Triangle3(c_origin+dec, c1+dec, c2+dec),
        Triangle3(c4+dec, c2+dec, c7+dec),
        Triangle3(c6+dec, c2+dec, c7+dec),
        Triangle3(c6+dec, c2+dec, c_origin+dec),
        Triangle3(c6+dec, c3+dec, c_origin+dec),
        Triangle3(c3+dec, c1+dec, c_origin+dec),
        Triangle3(c3+dec, c1+dec, c5+dec),
        Triangle3(c4+dec, c1+dec, c5+dec),
        Triangle3(c4+dec, c7+dec, c5+dec),
        Triangle3(c5+dec, c7+dec, c3+dec),
        Triangle3(c6+dec, c7+dec, c3+dec),

    ]
    # origine.replace(Coord3(0,0,30))
    print(t3.point1 is c_origin)
    print(f"main: triangles3:{time()-t_timeeee:.4f}s")
    t_timeeee = time()
    list_triangles2 = [p.project_Triangle3(t3) for t3 in list_triangles3]
    print(f"main: triangles2:{time()-t_timeeee:.4f}s")
    t_timeeee = time()
    img = Image(600, 400)
    print(f"main: creation img:{time()-t_timeeee:.4f}s")
    tttt = time()
    timeee1 = 0
    timeee2 = 0
    timeee3 = 0
    for t2 in list_triangles2:
        # t2.draw_better(img,(255,255,255))
        timeee1 += time()-t_timeeee
        t_timeeee = time()
        t2.draw_points(img)
        timeee2 += time()-t_timeeee
        t_timeeee = time()
        t2.draw_segments(img, col=(0, 0, 255))
        timeee3 += time()-t_timeeee
        t_timeeee = time()
    print(f"main: draw:{timeee1:.4f}s")
    print(f"main: draw_points:{timeee2:.4f}s")
    print(f"main: draw_segments:{timeee3:.4f}s")
    print(f"main: draw_total:{time()-tttt:.4f}s")
    t_timeeee = time()
    img.to_image("triangle.png")
    print(f"main: write:{time()-t_timeeee:.4f}s")
    print("main: fin")


    # test Parallelepidedon
    t= time()
    parelo = Parallelepidedon(Coord3(0,0,0),Coord3(10,10,10))
    img = Image(600, 400)
    parelo.drawlines(img)
    for i in range(10000):
        parelo = Parallelepidedon.randomOne()
        parelo.drawlines(img)
    img.to_image("parelo.png")
    print(f"main: parallelepipedon:{time()-t:.4f}s")
