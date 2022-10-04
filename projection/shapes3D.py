from typing import Union
import math
from images2D import Coord2,Triangle2

class Coord3():
    def __init__(self, abs, ord, hei) -> None:
        self.abs = abs
        self.ord = ord
        self.hei = hei

    def __repr__(self) -> str:
        return f"({self.abs},{self.ord},{self.hei})"

    def __eq__(self, __o: "Coord3") -> bool:
        return self.abs == __o.abs and self.ord == __o.abs and self.hei == __o.hei

    def __ne__(self, __o: object) -> bool:
        return not(self == __o)

    def __len__(self):
        return math.sqrt(self.abs**2+self.ord**2+self.hei**2)

    def __add__(self, __o: "Coord3") -> "Coord3":
        return Coord3(self.abs+__o.abs, self.ord+__o.ord, self.hei+__o.hei)

    def __neg__(self) -> "Coord3":
        return Coord3(-self.abs, -self.ord, -self.hei)

    def __sub__(self, __o: "Coord3") -> "Coord3":
        return Coord3(self.abs-__o.abs, self.ord-__o.ord, self.hei-__o.hei)

    def __mul__(self, k: int) -> "Coord3":
        return Coord3(self.abs*k, self.ord*k, self.hei*k)


class Triangle3():
    def __init__(self, point1: Coord3, point2: Coord3, point3: Coord3):
        self.point1 = point1
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

    def __mul__(self, other: "int"):
        if isinstance(other, Triangle3):
            return Triangle3(self.point1 * other.point1, self.point2 * other.point2, self.point3 * other.point3)
        return Triangle3(self.point1 * other, self.point2 * other, self.point3 * other)

    def __sub__(self, other: "Triangle3"):
        if isinstance(other, Triangle3):
            return Triangle3(self.point1 - other.point1, self.point2 - other.point2, self.point3 - other.point3)
        return Triangle3(self.point1 - other, self.point2 - other, self.point3 - other)


class Plan3():
    EP=0.001
    def __init__(self, x, y, z, const) -> None:
        self.relation = lambda c: c.abs*x+c.ord*y+c.hei*z+const
        self.point=Coord3(x,y,z)
        self.cst=const

    def __contains__(self,c:Union["Coord3","Coord2"]):
        return math.abs(self.relation(c))<=Plan3.EP if type(c) is Coord3 else math.abs(self.relation(Coord3(c.abs,c.ord,0)))<=Plan3.EP

    