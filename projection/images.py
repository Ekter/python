"""a module to create images with shapes"""
import math
from typing import List
import cv2 as cv
import numpy as np

class Coord2():
    """Vec2D object, created by rectangular or polar coordinates(with int coords in normal
    condition, but if broken, can have floats.(used for the moving anims))"""

    def __init__(self, abscisse: float, ordonnee: float, angle=False, broken=False):
        if not angle:
            self.abs = abscisse
            self.ord = ordonnee
        else:
            self.abs = abscisse * math.cos(ordonnee)
            self.ord = abscisse * math.sin(ordonnee)
        if not broken:
            self.abs = self.abs
            self.ord = self.ord

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
            return Coord2(self.abs + other.abs, self.ord + other.ord, broken=True)
        return Coord2(self.abs + other, self.ord + other)

    def __neg__(self):
        return Coord2(-self.abs, -self.ord, broken=True)

    def __mul__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs * other.abs, self.ord * other.ord, broken=True)
        return Coord2(self.abs * other, self.ord * other)

    def __sub__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs - other.abs, self.ord - other.ord, broken=True)
        return Coord2(self.abs - other, self.ord - other)

    def __abs__(self):
        return Coord2(abs(self.abs), abs(self.ord), broken=True)

    def __floordiv__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs / other.abs, self.ord / other.ord, broken=True)
        return Coord2(self.abs / other, self.ord / other)

    def __truediv__(self, other: "Coord2"):
        if isinstance(other, Coord2):
            return Coord2(self.abs / other.abs, self.ord / other.ord, broken=True)
        return Coord2(self.abs / other, self.ord / other)

    def __len__(self) -> float:
        return math.sqrt(self.abs ** 2 + self.ord ** 2)

    def __lt__(self, other: "Coord2") -> bool:
        if isinstance(other, Coord2):
            return len(self) < len(other)
        return len(self) < other

    def __gt__(self, other: "Coord2") -> bool:
        if isinstance(other, Coord2):
            return len(self) > len(other)
        return len(self) > other

    def __le__(self, other: "Coord2") -> bool:
        if isinstance(other, Coord2):
            return len(self) <= len(other)
        return len(self) <= other

    def __ge__(self, other: "Coord2") -> bool:
        if isinstance(other, Coord2):
            return len(self) >= len(other)
        return len(self) >= other

    def getangle(self) -> float:
        """returns the angle of the vector (self.abs, self.ord)"""
        return math.atan2(self.ord, self.abs)

    def ind(self) -> tuple:
        """returns a tuple (abs,ord). Used for """
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

class Segment2(Coord2):
    """A segment is a line between two points"""

    def __init__(self, point1: Coord2, point2: Coord2):
        self.point1 = point1
        self.point2 = point2
        e=(point2.ord-point1.ord)/(point2.abs-point1.abs)
        self.function = lambda x: e*x+point1.ord-e*point1.abs

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

    def under(self,point:Coord2)->bool:
        return self.function(point.abs) <= point.ord
    # TODO def intersect(self,other:"Segment2") -> Coord2:

class Triangle():
    """A triangle is a set of three points"""

    def __init__(self, point1: Coord2, point2: Coord2, point3: Coord2):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def __repr__(self) -> str:
        return "Triangle(" + str(self.point1) + "," + str(self.point2) + "," + str(self.point3) + ")"

    def __eq__(self, other: "Triangle") -> bool:
        return (
            self.point1 == other.point1
            and self.point2 == other.point2
            and self.point3 == other.point3
            if isinstance(other, Triangle)
            else False
        )

    def __ne__(self, other: "Triangle") -> bool:
        return not self == other

    def __add__(self, other: "Triangle"):
        if isinstance(other, Triangle):
            return Triangle(
                self.point1 + other.point1,
                self.point2 + other.point2,
                self.point3 + other.point3,
            )
        return Triangle(self.point1 + other, self.point2 + other, self.point3 + other)

    def __neg__(self):
        return Triangle(-self.point1, -self.point2, -self.point3)

    def __mul__(self, other: "int"):
        if isinstance(other, Triangle):
            return Triangle(self.point1 * other.point1, self.point2 * other.point2, self.point3 * other.point3)
        return Triangle(self.point1 * other, self.point2 * other, self.point3 * other)

    def __sub__(self, other: "Triangle"):
        if isinstance(other, Triangle):
            return Triangle(self.point1 - other.point1, self.point2 - other.point2, self.point3 - other.point3)
        return Triangle(self.point1 - other, self.point2 - other, self.point3 - other)

    def segments(self) -> List[Segment2]:
        "Returns the three segments of the triangle"
        return [
            Segment2(self.point1, self.point2),
            Segment2(self.point2, self.point3),
            Segment2(self.point3, self.point1),
        ]

    def __contains__(self,point:Coord2) -> bool:
        "Returns True if the point is in the triangle"
        return sum([segment.under(point) for segment in self.segments()]) == 1 and min(self.point1.abs,self.point2.abs,self.point3.abs)<=point.abs<=max(self.point1.abs,self.point2.abs,self.point3.abs)



p1=Coord2(10,10)
print(p1)
p2=Coord2(450,200)
print(p2)
p3=Coord2(200,900)
print(p3)
t=Triangle(p1,p2,p3)
print(t)
print(p1 in t)
def triangle(lenght: int, weight: int):
    matrice = [[(0, 0, 0) for _ in range(lenght)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(weight):
            # a, b, c = matrice[i][j]
            d=int(Coord2(i,j) in t)*255
            matrice[i][j] = (d,d,d)
    return matrice
cv.imwrite(f"triangle.png", np.array(triangle(1000, 1000)))
