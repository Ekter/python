"""a module to create images with shapes"""
import math
import time
from typing import List, Tuple
import cv2 as cv
import numpy as np
import random


class Coord2():
    """Vec2D object, created by rectangular or polar coordinates(with int coords in normal
    condition, but if broken, can have floats.(used for the moving anims))"""

    def __init__(self, abscisse: float, ordonnee: float, angle=False):
        if not angle:
            self.abs = abscisse
            self.ord = ordonnee
        else:
            self.abs = abscisse * math.cos(ordonnee)
            self.ord = abscisse * math.sin(ordonnee)

    def __repr__(self) -> str:
        return "<" + str(self.abs) + "," + str(self.ord) + ">"

    def __eq__(self, other: "Coord2") -> bool:
        return (
            self.abs == other.abs and self.ord == other.ord
            if isinstance(other, Coord2)
            else len(self) == other
        )

    def __ne__(self, other: "Coord2") -> bool:
        return not self == other

    def __add__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs + other.abs, self.ord + other.ord)
        return Coord2(self.abs + other, self.ord + other)

    def __neg__(self):
        return Coord2(-self.abs, -self.ord)

    def __mul__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs * other.abs, self.ord * other.ord)
        return Coord2(self.abs * other, self.ord * other)

    def __sub__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs - other.abs, self.ord - other.ord)
        return Coord2(self.abs - other, self.ord - other)

    def __abs__(self):
        return Coord2(abs(self.abs), abs(self.ord))

    def __floordiv__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs / other.abs, self.ord / other.ord)
        return Coord2(self.abs / other, self.ord / other)

    def __truediv__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs / other.abs, self.ord / other.ord)
        return Coord2(self.abs / other, self.ord / other)

    def __len__(self) -> float:
        return math.sqrt(self.abs ** 2 + self.ord ** 2)

    def getangle(self) -> float:
        """returns the angle of the vector (self.abs, self.ord)"""
        return math.atan2(self.ord, self.abs)

    def ind(self) -> tuple:
        """returns a tuple (abs,ord). Used for ?"""
        return self.abs, self.ord

    def distance(self, other: "Coord2") -> float:
        "Diagonal distance between two points"
        return (self - other).__len__()

    def dirtrig(self):
        "Direction from the center to a point"
        if self == Coord2(0, 0):
            return Coord2(0, 0)
        cos = self.abs / self.__len__()
        if cos > 1 / math.sqrt(2) - 0.1:
            return Coord2(-1, 0)
        if cos < -1 / math.sqrt(2) + 0.1:
            return Coord2(1, 0)
        if self.ord > 0:
            return Coord2(0, -1)
        return Coord2(0, 1)

    def cosinus(self, other: "Coord2"):
        """returns the cosine of a coord (adj/hyp)"""
        return (self - other).abs / (self - other).__len__()

    def direction(self, other: "Coord2"):
        "Direction from a point to another"
        return (self - other).dirtrig()

    def inverse(self):
        "Inverse of a Coord(swapping x and y)"
        return Coord2(self.ord, self.abs)

    def coin1(self, other: "Coord2"):
        "First combinaison of two Coords"
        return Coord2(self.abs, other.ord)

    def coin2(self, other: "Coord2"):
        "Second combinaison of two Coords"
        return Coord2(other.abs, self.ord)

    def middle(self, other: "Coord2"):
        "Middle of two Coords"
        return (self + other) // 2

    def facing(self):
        "Function to choose the correct direction of an image"
        direction = self.dirtrig()
        if direction == Coord2(0, 1):
            return 1
        if direction == Coord2(1, 0):
            return 2
        if direction == Coord2(-1, 0):
            return 3
        return 0

    @staticmethod
    def randomCoord2(x: int = 1000, y: int = 1000):
        return Coord2(random.randint(0, x), random.randint(0, y))


class Segment2(Coord2):
    """A segment is a line between two points"""

    def __init__(self, point1: Coord2, point2: Coord2):
        if point1.abs==point2.abs:
            point2.abs+=0.000001
        self.point1 = point1
        self.point2 = point2
        self.coeff = (point2.ord-point1.ord)/(point2.abs-point1.abs)
        self.function = lambda x: self.coeff*x+point1.ord-self.coeff*point1.abs

    def __repr__(self) -> str:
        return "Segment2(" + str(self.point1) + "," + str(self.point2) + ")"

    def __eq__(self, other: "Segment2") -> bool:
        return (
            self.point1 == other.point1 and self.point2 == other.point2
            if isinstance(other, Segment2)
            else False
        )

    def __ne__(self, other: "Segment2") -> bool:
        return not self == other

    def __add__(self, other: "Segment2"):
        if isinstance(other, Segment2):
            return Segment2(self.point1 + other.point1, self.point2 + other.point2)
        return Segment2(self.point1 + other, self.point2 + other)

    def __neg__(self):
        return Segment2(-self.point1, -self.point2)

    def __mul__(self, other: "int"):
        if isinstance(other, Segment2):
            return Segment2(self.point1 * other.point1, self.point2 * other.point2)
        return Segment2(self.point1 * other, self.point2 * other)

    def __sub__(self, other: "Segment2"):
        if isinstance(other, Segment2):
            return Segment2(self.point1 - other.point1, self.point2 - other.point2)
        return Segment2(self.point1 - other, self.point2 - other)

    def __abs__(self):
        return Segment2(abs(self.point1), abs(self.point2))

    def __len__(self) -> float:
        return self.point1.distance(self.point2)

    def under(self, point: Coord2) -> bool:
        return self.function(point.abs) <= point.ord
    # TODO def intersect(self,other:"Segment2") -> Coord2:


class Triangle2():
    """A triangle is a set of three points"""

    def __init__(self, point1: Coord2, point2: Coord2, point3: Coord2):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.rangex = range(min(self.point1.abs, self.point2.abs, self.point3.abs), max(
            self.point1.abs, self.point2.abs, self.point3.abs))
        self.rangey = range(min(self.point1.ord, self.point2.ord, self.point3.ord), max(
            self.point1.ord, self.point2.ord, self.point3.ord))

    def __repr__(self) -> str:
        return "Triangle[" + str(self.point1) + "," + str(self.point2) + "," + str(self.point3) + "]"

    def __eq__(self, other: "Triangle2") -> bool:
        return (
            self.point1 == other.point1
            and self.point2 == other.point2
            and self.point3 == other.point3
            if isinstance(other, Triangle2)
            else False
        )

    def __ne__(self, other: "Triangle2") -> bool:
        return not self == other

    def __add__(self, other: "Triangle2"):
        if isinstance(other, Triangle2):
            return Triangle2(
                self.point1 + other.point1,
                self.point2 + other.point2,
                self.point3 + other.point3,
            )
        return Triangle2(self.point1 + other, self.point2 + other, self.point3 + other)

    def __neg__(self):
        return Triangle2(-self.point1, -self.point2, -self.point3)

    def __mul__(self, other: int):
        if isinstance(other, Triangle2):
            return Triangle2(self.point1 * other.point1, self.point2 * other.point2, self.point3 * other.point3)
        return Triangle2(self.point1 * other, self.point2 * other, self.point3 * other)

    def __sub__(self, other: "Triangle2"):
        if isinstance(other, Triangle2):
            return Triangle2(self.point1 - other.point1, self.point2 - other.point2, self.point3 - other.point3)
        return Triangle2(self.point1 - other, self.point2 - other, self.point3 - other)

    def segments(self) -> List[Segment2]:
        "Returns the three segments of the triangle"
        return [
            Segment2(self.point1, self.point2),
            Segment2(self.point2, self.point3),
            Segment2(self.point3, self.point1),
        ]

    def points(self) -> List[Coord2]:
        "Returns the three points of the triangle"
        return [self.point3, self.point1, self.point2]

    def enumerate(self) -> Tuple[Segment2, Coord2]:
        "Yields the three points of the triangle, with their segments"
        yield (Segment2(self.point1, self.point2), self.point3)
        yield (Segment2(self.point2, self.point3), self.point1)
        yield (Segment2(self.point3, self.point1), self.point2)

    def __contains__(self, point: Coord2) -> bool:
        "Returns True if the point is in the triangle"
        # and min(self.point1.abs,self.point2.abs,self.point3.abs)<=point.abs<=max(self.point1.abs,self.point2.abs,self.point3.abs)
        return sum([segment.under(point) == segment.under(pointtri) for segment, pointtri in self.enumerate()]) == 3

    @staticmethod
    def randomTriangle(x: int = 1000, y: int = 1000):
        return Triangle2(Coord2.randomCoord2(x, y), Coord2.randomCoord2(x, y), Coord2.randomCoord2(x, y))

    def draw(self, length: int, heigth: int, col=(255, 255, 255), mat=None):
        matrice = [[(0, 0, 0) for _ in range(length)]
                   for _ in range(length)] if mat is None else mat.copy()
        for i in self.rangex:
            for j in self.rangey:
                a, b, c = matrice[i][j]
                if Coord2(i, j) in self:
                    matrice[i][j] = col
        return matrice

    def draw_shaders(self, length: int, heigth: int, col=(255, 255, 255), mat=None):
        matrice = [[(0, 0, 0) for _ in range(length)]
                   for _ in range(heigth)] if mat is None else mat.copy()
        for i in self.rangex:
            for j in self.rangey:
                a, b, c = matrice[i][j]
                if Coord2(i, j) in self:
                    matrice[i][j] = col
        mat2=matrice.copy()
        for i in self.rangex:
            for j in self.rangey:
                a1, b1, c1 = matrice[i][j-2] if j-2>=0 else (0,0,0)
                a2, b2, c2 = matrice[i][j+2] if j+2<heigth else (0,0,0)
                a3, b3, c3 = matrice[i][j-1] if j-1>=0 else (0,0,0)
                a4, b4, c4 = matrice[i][j+1] if j+1<heigth else (0,0,0)
                a5, b5, c5 = matrice[i][j]
                mat2[i][j]=[(a1*0.1+a2*0.1+a3*0.2+a4*0.2+a5*0.4),(b1*0.1+b2*0.1+b3*0.2+b4*0.2+b5*0.4),(c1*0.1+c2*0.1+c3*0.2+c4*0.2+c5*0.4)]

        return matrice

    def drawpoints(self, col=(255, 0, 0), mat=None):
        matrice = [[(0, 0, 0) for _ in range(500)]
                   for _ in range(500)] if mat is None else mat.copy()
        for point in self.points:
            for i in range(-2, 3, 1):
                try:
                    matrice[point.abs+i][point.ord] = col
                except:
                    print("limite")
                try:
                    matrice[point.abs][point.ord+i] = col
                except:
                    print("limite")
            try:
                matrice[point.abs][point.ord] = col
            except:
                print("limite")
        return matrice

print(type(Triangle2.randomTriangle))
if __name__ == "__main__":
    p1 = Coord2(10, 10)
    print(p1)
    p2 = Coord2(450, 201)
    print(p2)
    p3 = Coord2(200, 900)
    print(p3)
    tri = Triangle2(p1, p2, p3)
    print(tri)
    print(tri.rangex)

    print(p1 in tri)

    sizemax = 100
    sizetri = 100
    num = 50
    num2=1
    delay = 0.05
    tott = 0
    ttot = time.time()
    for j in range(num2):
        t = time.time()
        for _ in range(num):
            ar = np.array(Triangle2.randomTriangle(
                sizetri, sizetri).draw(sizemax, sizemax))
            cv.imwrite(f"triangle.png", ar)
            time.sleep(delay)
            matrice = [[(0, 0, 0) for _ in range(sizemax)]
                       for _ in range(sizemax)]
            b = np.array(matrice)
        tott += (time.time()-t)/num  # t-num*delay
    print(tott/num2)
    print(time.time()-ttot)

    ttot = time.time()
    for j in range(num2):
        t = time.time()
        for _ in range(num):
            ar = np.array(Triangle2.randomTriangle(
                sizetri, sizetri).draw_shaders(sizemax, sizemax))
            cv.imwrite(f"triangle.png", ar)
            time.sleep(delay)
            matrice = [[(0, 0, 0) for _ in range(sizemax)]
                       for _ in range(sizemax)]
            b = np.array(matrice)
        tott += (time.time()-t)/num  # t-num*delay
    print(tott/num2)
    print(time.time()-ttot)
