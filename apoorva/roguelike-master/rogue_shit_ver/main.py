class Element:
    def __init__(self, name, abbrv=None):
        self.name = name
        if abbrv:
            self.abbrv = abbrv
        else:
            self.abbrv = name[0]

    def __repr__(self):
        return self.abbrv

    def description(self):
        return f"<{self.name}>"

    def meet(self, hero):
        hero.take(self)
        return False


class Creature(Element):
    def __init__(self, name, hp, abbrv=None, strength=None):
        super().__init__(name, abbrv=abbrv)
        self.hp = hp
        if strength:
            self.strength = strength
        else:
            self.strength = 1

    def description(self):
        return Element.description(self) + f"({self.hp})"

    def meet(self, hero):
        self.hp -= hero.strength
        if self.hp > 0:
            hero.hp -= self.strength
            return False
        else:
            return True


class Hero(Creature):
    def __init__(self, name='Hero', hp=None, abbrv='@', strength=2):
        if not hp:
            hp = 10
        super().__init__(name, hp, abbrv=abbrv, strength=strength)
        self._inventory = []

    def take(self, element):
        self._inventory.append(element)

    def description(self):
        return Creature.description(self) + str(self._inventory)


h = Hero()
o = Creature("Ork", 3)
print(o.meet(h))
print(h.description())
print(o.description())
print(o.meet(h))
print(h.description())
print(o.description())

print()
print()
h = Hero(hp=3, strength=10)
o = Creature("Ork", strength=10, hp=12)
print(o.meet(h))
print(h.description())
print(o.description())
