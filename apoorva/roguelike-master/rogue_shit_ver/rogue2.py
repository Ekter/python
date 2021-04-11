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
    def __init__(self, name, abbrv=""):
        self.name = name
        if abbrv == "":
            abbrv = name[0]
        self.abbrv = abbrv

    def __repr__(self):
        return self.abbrv

    def description(self):
        return "<" + str(self.name) + ">"

    def meet(self, hero):
        hero.take(self)
        return True


class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)


class Room:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def center(self):
        return Coord((self.c2.x - self.c1.x) // 2 + self.c1.x, (self.c2.y - self.c1.y) // 2 + self.c1.y)

    def __repr__(self):
        return f"[<{self.c1.x},{self.c1.y}>, <{self.c2.x},{self.c2.y}>]"

    def __contains__(self, item):
        if isinstance(item, Coord):
            return self.c1.x <= item.x <= self.c2.x and self.c1.y <= item.y <= self.c2.y
        return False

    def intersect(self, other):
        corner_coord = [other.c1, other.c2, Coord(other.c1.x, other.c2.y), Coord(other.c2.x, other.c1.y)]
        for coord in corner_coord:
            if coord in self:
                return True

        our_coords = [self.c1, self.c2, Coord(self.c1.x, self.c2.y), Coord(self.c2.x, self.c1.y)]
        for coord in our_coords:
            if coord in other:
                return True
        return False


class Creature(Element):
    def __init__(self, name, hp, abbrv="", strength=1):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.strength = strength

    def description(self):
        return Element.description(self) + "(" + str(self.hp) + ")"

    def meet(self, hero):
        self.hp -= hero.strength
        if self.hp > 0:
            hero.hp -= self.strength
            return False
        return True


class Hero(Creature):
    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []

    def description(self):
        return Creature.description(self) + str(self._inventory)

    def take(self, elem):
        self._inventory.append(elem)


class Map(object):
    ground = '.'
    empty = ' '
    dir = {'z': Coord(0, -1), 's': Coord(0, 1), 'd': Coord(1, 0), 'q': Coord(-1, 0)}
    _roomsToReach = []
    _rooms = []

    def __init__(self, size=20, pos=Coord(1, 1), hero=None):
        self._mat = []
        self._elem = {}
        for k in range(size):
            self._mat.append([Map.empty] * size)
        if hero is None:
            hero = Hero()
        self.hero = hero
        self.put(pos, hero)

    def addRoom(self, room):
        if isinstance(room, Room):
            Map._roomsToReach.append(Room)
            for y in range(room.c1.y, room.c2.y):
                for x in range(room.c1.x, room.c2.x):
                    self._mat[y][x] = Map.ground

    # o est l'élément, e est la case/cellule
    def put(self, e, o):
        self._mat[e.y][e.x] = o
        self._elem[o] = e

    def __len__(self):
        return len(self._mat)

    def __repr__(self):
        a = ""
        for i in self._mat:
            for j in i:
                a = a + str(j)
            a = a + '\n'
        return a

    def __contains__(self, item):
        if isinstance(item, Coord):
            return 0 <= item.x < len(self) and 0 <= item.y < len(self)
        return item in self._elem

    def get(self, e):
        return self._mat[e.y][e.x]

    def pos(self, o):
        return self._elem[o]

    def rm(self, e):
        del self._elem[self.get(e)]
        self._mat[e.y][e.x] = Map.ground

    def move(self, e, way):
        dest = self.pos(e) + way
        if dest in self:
            if self.get(dest) == Map.ground:
                self.rm(self.pos(e))
                self.put(dest, e)
            elif self.get(dest).meet(e):
                self.rm(dest)

    def play(self):
        print("--- Welcome Hero! ---")
        while self.hero.hp > 0:
            print()
            print(self)
            print(self.hero.description())
            self.move(self.hero, Map.dir[getch()])
        print("--- Game Over ---")


print(Map(3)._mat)
print(Map()._elem)
print(Map.empty == " ")
print(Map()._rooms)
print(Map()._roomsToReach)
