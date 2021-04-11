import keyboard
import pygame
import os


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"<{self.x},{self.y}>"


class Map:
    def __init__(self, ground='.', size=5, pos=Coord(1, 1), hero="@"):
        self.hero = hero
        self.hero_pos = pos
        self.size = size
        self.ground = ground
        self.dir = {
            'w': Coord(0, -1),
            's': Coord(0, 1),
            'd': Coord(1, 0),
            'a': Coord(-1, 0),
        }
        self._mat = []
        for _ in range(self.size):
            self._mat.append(['.'] * self.size)
        self._elem = {}

        self._mat[pos.y][pos.x] = self.hero
        self._elem['@'] = self.hero_pos

    def __repr__(self):
        string = ''
        for y in self._mat:
            for x in y:
                string += x
            string += '\n'
        return string

    def __len__(self):
        return self.size

    def __contains__(self, item):
        if isinstance(item, Coord):
            if 0 <= item.x < self.size and 0 <= item.y < self.size:
                return True
            else:
                return False
        else:
            for y in self._mat:
                for x in y:
                    if x == item:
                        return True
            return False

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(value, key)

    def get(self, coord):
        if isinstance(coord, Coord):
            try:
                return self._mat[coord.y][coord.x]
            except IndexError as e:
                print(e)

    def pos(self, element):
        for y, y_ele in enumerate(self._mat):
            for x, x_ele in enumerate(y_ele):
                if x_ele == element:
                    return Coord(x, y)

    def put(self, coord, element):
        if isinstance(coord, Coord):
            try:
                if self._mat[coord.y][coord.x] == self.ground:
                    self._mat[coord.y][coord.x] = element
                    self._elem[element] = coord
                else:
                    raise IndexError(f"{self._mat[coord.y][coord.x]} is at that position cannot put {element} there")
            except IndexError as e:
                print(e)

    def rm(self, coord):
        if isinstance(coord, Coord):
            try:
                if self._mat[coord.y][coord.x] != self.ground:
                    del self._elem[self._mat[coord.y][coord.x]]
                    self._mat[coord.y][coord.x] = self.ground
                else:
                    raise IndexError(f"{self._mat[coord.y][coord.x]} there is nothing here at {coord}")
            except IndexError as e:
                print(e)

    def move(self, element, direction):
        position = self.pos(element)
        new_pos = position + direction
        if new_pos in self:
            if self._mat[new_pos.y][new_pos.x] == self.ground:
                self.rm(position)
                self.put(new_pos, element)

    def move_hero(self, input):
        self.move(self.hero, self.dir[input])


def main():
    map = Map(size=20)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        if keyboard.is_pressed("w"):
            map.move(map.hero, map.dir["w"])
        if keyboard.is_pressed("a"):
            map.move(map.hero, map.dir["a"])
        if keyboard.is_pressed("s"):
            map.move(map.hero, map.dir["s"])
        if keyboard.is_pressed("d"):
            map.move(map.hero, map.dir["d"])
        print(map)


main()
