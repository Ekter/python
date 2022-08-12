#!/usr/bin/python3
#                               MIND MAZE
# Roguelike project, by Nino Mulac, Ilane Pelletier, Arwen Duee-Moreau, Hugo Durand, Vaiki Martelli, and Kylian Girard
import time
import random
from typing import Any, Callable, List, Union, Optional
import tkinter
import copy
import math
import constants
import utils
import images


class Coord():
    """Vec2D object, created by rectangular or polar coordinates(with int coords in normal
    condition, but if broken, can have floats.(used for the moving anims)"""

    def __init__(self, abscisse: int, ordonnee: int, angle=False, broken=False):
        if not angle:
            self.abs = abscisse
            self.ord = ordonnee
        else:
            self.abs = abscisse * math.cos(ordonnee)
            self.ord = abscisse * math.sin(ordonnee)
        if not broken:
            self.abs = int(self.abs)
            self.ord = int(self.ord)

    def __repr__(self) -> str:
        return "<" + str(self.abs) + "," + str(self.ord) + ">"

    def __eq__(self, other: "Coord") -> bool:
        return (
            self.abs == other.abs and self.ord == other.ord
            if isinstance(other, Coord)
            else len(self) == other
        )

    def __ne__(self, other: "Coord") -> bool:
        return not self == other

    def __add__(self, other: "Coord"):
        if isinstance(other, Coord):
            return Coord(self.abs + other.abs, self.ord + other.ord, broken=True)
        return Coord(self.abs + other, self.ord + other)

    def __neg__(self):
        return Coord(-self.abs, -self.ord, broken=True)

    def __mul__(self, other: "Coord"):
        if isinstance(other, Coord):
            return Coord(self.abs * other.abs, self.ord * other.ord, broken=True)
        return Coord(self.abs * other, self.ord * other)

    def __sub__(self, other: "Coord"):
        if isinstance(other, Coord):
            return Coord(self.abs - other.abs, self.ord - other.ord, broken=True)
        return Coord(self.abs - other, self.ord - other)

    def __abs__(self):
        return Coord(abs(self.abs), abs(self.ord), broken=True)

    def __floordiv__(self, other: "Coord"):
        if isinstance(other, Coord):
            return Coord(self.abs / other.abs, self.ord / other.ord, broken=True)
        return Coord(self.abs / other, self.ord / other)

    def __truediv__(self, other: "Coord"):
        if isinstance(other, Coord):
            return Coord(self.abs / other.abs, self.ord / other.ord, broken=True)
        return Coord(self.abs / other, self.ord / other)

    def __len__(self) -> float:
        return math.sqrt(self.abs ** 2 + self.ord ** 2)

    def __lt__(self, other: "Coord") -> bool:
        if isinstance(other, Coord):
            return len(self) < len(other)
        return len(self) < other

    def __gt__(self, other: "Coord") -> bool:
        if isinstance(other, Coord):
            return len(self) > len(other)
        return len(self) > other

    def __le__(self, other: "Coord") -> bool:
        if isinstance(other, Coord):
            return len(self) <= len(other)
        return len(self) <= other

    def __ge__(self, other: "Coord") -> bool:
        if isinstance(other, Coord):
            return len(self) >= len(other)
        return len(self) >= other

    def __iter__(self):
        for i in (self.abs, self.ord):
            yield i

    def __hash__(self) -> int:
        return hash((self.abs, self.ord))

    def getangle(self) -> float:
        """returns the angle of the vector (self.abs, self.ord)"""
        return math.atan2(self.ord, self.abs)

    def ind(self) -> tuple:
        """returns a tuple (abs,ord). Used for """
        return self.abs, self.ord

    def distance(self, other: "Coord") -> float:
        "Diagonal distance between two points"
        return (self - other).__len__()

    def dirtrig(self):
        "Direction from the center to a point"
        if self == Coord(0, 0):
            return Coord(0, 0)
        cos = self.abs / self.__len__()
        if cos > 1 / math.sqrt(2) - 0.1:
            return Coord(-1, 0)
        if cos < -1 / math.sqrt(2) + 0.1:
            return Coord(1, 0)
        if self.ord > 0:
            return Coord(0, -1)
        return Coord(0, 1)

    def cosinus(self, other: "Coord"):
        """returns the cosine of a coord (adj/hyp)"""
        return (self - other).abs / (self - other).__len__()

    def direction(self, other: "Coord"):
        "Direction from a point to another"
        return (self - other).dirtrig()

    def inverse(self):
        "Inverse of a Coord(swapping x and y)"
        return Coord(self.ord, self.abs)

    def coin1(self, other: "Coord"):
        "First combinaison of two Coords"
        return Coord(self.abs, other.ord)

    def coin2(self, other: "Coord"):
        "Second combinaison of two Coords"
        return Coord(other.abs, self.ord)

    def middle(self, other: "Coord"):
        "Middle of two Coords"
        return (self + other) // 2

    def facing(self):
        "Function to choose the correct direction of an image"
        direction = self.dirtrig()
        if direction == Coord(0, 1):
            return 1
        if direction == Coord(1, 0):
            return 2
        if direction == Coord(-1, 0):
            return 3
        return 0


class CoordScreen(Coord):
    "A Coord, but defined by its place on the screen."

    def __init__(self, x: float, y: float):
        Coord.__init__(self, x * 1080, y * 800, broken=True)


class Status():
    "Status affecting a creature each turn, making it lose points from a stat"

    def __init__(self, name, turns, effect, target="hp", prb=1):
        self.name = name
        self.target = target
        self.effect = effect
        self.prb = prb
        self.turns = turns

    def __str__(self) -> str:
        return self.name + " " + str(self.turns) + " " + str(self.effect) + " " + str(
            self.target) + " " + str(self.prb)

    def __eq__(self, other: "Status") -> bool:
        return (
            self.name == other.name
            and self.turns == other.turns
            and self.effect == other.effect
            and self.target == other.target
            and self.prb == other.prb
        )

    def __ne__(self, other: "Status") -> bool:
        return not self == other


class Element():
    """Basic Element of the roguelike. Childs must implement meet(Creature)."""

    def __init__(self, name: str, abbrv: str = None, transparent: bool = False, f: bool = False):
        self.name = name
        self.transparent = transparent
        self.abbrv = name[0] if abbrv is None else abbrv
        if abbrv is None:
            self.abbrv = name[0]
        else:
            self.abbrv = abbrv
        self.is_f = f
        del self

    def __repr__(self) -> str:
        return self.abbrv

    def description(self) -> str:
        "Description of the Element"
        return "<{}>".format(self.name)

    def meet(self, other: "Creature", distant=False):
        "Warning! Not defined for Elements yet!"
        raise NotImplementedError(f"""Not implemented yet:
            {self} can't meet {other} at distance {distant}""")

    def accord(self):
        "returns {e name} if is_f else just { name} (pour les accords 'un'/'une')"
        return f"e {self.name}" if self.is_f else f" {self.name}"


class Decoration(Element):
    "Just a decoration."

    def __init__(self, name, abbrv=None, transparent=False):
        Element.__init__(self, name, abbrv, transparent)

    def meet(self, other: "Creature", distant=False):
        "useless function called when a creature bumps a decoration"
        return False


class Creature(Element):
    "Element with hps and strength, movable in a Map"

    def __init__(
        self,
        name: str,
        hp: int,
        abbrv: str = None,
        strength: int = 1,
        defense: int = 0,
        inventory: List["Equipment"] = None,
        equips: List["Equipment"] = None,
        bourse: int = 0,
        vitesse: int = 1,
        level: int = 1,
        action: int = 0,
        power: List[Status] = None,
        special: Optional[Callable[["Creature"], None]] = None,
        distantstrenght: int = 0,
    ):
        super().__init__(self, name, abbrv)#,( transparent=True)
        self.hp = int(hp * (1.5 ** level))
        self.hpmax = self.hp
        self.level = level
        self.strength = int(strength * (1.5 ** level))
        self.defense = int(defense * (1.5 ** level))
        self.absp = (self.hp + 3 * self.strength) * level
        self.bourse = bourse
        self.inventory = inventory if inventory is not None else []
        self.equips = equips if equips is not None else [
            None, None, None, None]
        self.listeffects = []
        self.dpl = []
        self.vitesse = vitesse
        self.facing = Coord(0, 0)
        self.action = action
        self.power = power
        self.special = special
        self.distantstrenght = distantstrenght

    def __contains__(self, item: Union[str, "Equipment"]):
        return (item in self.inventory) if isinstance(item, Equipment) else (item in [
            i.name for i in self.inventory])

    def description(self) -> str:
        "Description of the Creature"
        return Element.description(self) + f"({self.hp})*{self.level}*"

    def heal(self, heal_amount: int = 3) -> True:
        """Heals a creature"""
        self.hp = min(self.hpmax, self.hp + heal_amount)
        return True

    def meet(self, other: "Creature", distant: bool = False) -> bool:
        """Encounter between two creatures: the first(self) is attacked by the second(other).
            If distant, the first is attacked by the second's distant attack."""
        self.hp -= self.distantstrenght if distant else (
            other.strength - random.randint(0, self.defense))
        if other.power is not None:
            self.listeffects.append(other.power)
        theGame().addMessage(f"Le {other.name} frappe le {self.name}", life=1)
        if self.special is not None and isinstance(other, Hero):
            self.special(self)
        if other.special is not None and isinstance(self, Hero):
            other.special(other)
        if self.hp <= 0:
            return other.gainxp(self)
        return False

    def statuslose(self, status: Status) -> bool:
        "Make the Creature be affected by its statuses"
        if status.target in self.__dict__:
            if random.random() < status.prb:
                self.__dict__[status.target] += status.effect
            status.turns -= 1
            if status.turns > 0:
                return False
        else:
            theGame().addMessage("")
        return True

    def creaturn(self, mapp: "Floor") -> None:
        "Affect a creature with its statuses"
        for attack in mapp.getattacks():
            if mapp.getattacks()[attack] == mapp[self]:
                self.heal(attack.dmg)
                theGame().addMessage(str(attack.dmg))
                for i in attack.effects:
                    self.listeffects.append(i)
        newlist = []
        for status in self.listeffects:
            if not self.statuslose(status):
                newlist.append(status)
        self.listeffects = newlist

    def take(self, equip: "Equipment") -> bool:
        "Taking an Equipment: add it to the Creature's inventory"
        if len(self.inventory) <= (9 if isinstance(self, Hero) else 1):
            self.inventory.append(equip)
            return True
        return False

    def gainxp(self, creature: "Creature") -> True:
        "Killing a Creature makes you gain xp."
        self.absp += creature.absp/2
        if self.absp >= 5 + 5 * self.level:
            self.absp = 0
            self.levelup()
        return True

    def levelup(self) -> None:
        "Level up : stats are increased"
        self.hpmax += 2
        self.level += 1
        self.strength += 1
        self.hp = self.hpmax
        theGame().addMessage(
            f"Le {self.description()} a gagné un niveau!(niveau {self.level})"
        )

    def throw(self, equip: "Equipment") -> None:
        "Throws the item"
        devant = theGame()[self] + self.facing
        portee = 5
        while (
            (devant + self.facing in theGame().floor)
            and (
                theGame()[devant + self.facing] in Floor.listground
                or theGame()[devant + self.facing] in Floor.listgroundwet
            )
            and portee != 0
        ):
            devant += self.facing
            portee -= 1
        if ((devant + self.facing) in theGame().floor) and isinstance(
            theGame()[devant + self.facing], Creature
        ):
            theGame()[devant + self.facing].action += 8
        elif ((devant + self.facing) in theGame().floor) and (
            theGame()[devant + self.facing] in Floor.listground
            or theGame()[devant + self.facing] in Floor.listground
        ):
            theGame()[devant + self.facing] = equip if equip.used == "idem" else copy.copy(
                equip.used)
        elif ((devant + self.facing) in theGame().floor) and (
            isinstance(theGame()[devant + self.facing], Equipment)
            or theGame()[devant + self.facing] == Floor.empty
        ):
            theGame()[devant] = equip if equip.used == "idem" else copy.copy(
                equip.used)
        self.inventory.remove(equip)
        theGame().deselect()
        theGame().gameturn()

    def unhide(self, newabbrv: str) -> None:
        "Changes the abbrv of a creature. Useful for ghosts"
        self.abbrv = newabbrv

    def tir(self) -> None:
        devant = theGame().floor._creatures[self] + self.facing
        portee = 5
        if isinstance(theGame()[devant], Creature) and theGame()[devant].meet(self, distant=True):
            theGame().floor.rm(devant)
        else:
            while theGame()[devant + self.facing] in theGame().floor.listgrounds and portee != 0:
                if isinstance(theGame()[devant + self.facing], Creature):
                    theGame()[devant + self.facing].meet(self, distant=True)
                    portee = 0
                if (theGame()[devant + self.facing].meet(self)):
                    theGame().floor.rm(devant + self.facing)
                devant += self.facing
                portee -= 1


class Flying(Creature):
    def __init__(
        self,
        name: str,
        hp: int,
        abbrv: str = None,
        strength: int = 1,
        defense: int = 0,
        inventory: List["Equipment"] = None,
        equips: List["Equipment"] = None,
        bourse: int = 0,
        vitesse: int = 1,
        level: int = 1,
        action: int = 0,
        power: List[Status] = None,
        special: Optional[Callable[["Creature"], None]] = None,
        distantstrenght: int = 0,
    ):
        super().__init__(
            name,
            hp,
            abbrv,
            strength,
            defense,
            inventory,
            equips,
            bourse,
            vitesse,
            level,
            action,
            power,
            special,
            distantstrenght,
        )


class Archer(Creature):
    "An creature attacking the hero from far away"

    def __init__(
        self,
        name: str,
        hp: int,
        abbrv: str = None,
        strength: int = 1,
        defense: int = 0,
        inventory: List["Equipment"] = None,
        equips: List["Equipment"] = None,
        bourse: int = 0,
        vitesse: int = 1,
        level: int = 1,
        action: int = 0,
        power=None,
        special=None,
    ):
        Creature.__init__(
            self,
            name,
            hp,
            abbrv=abbrv,
            strength=strength,
            defense=defense,
            inventory=[] if inventory is None else inventory,
            equips=[None, None, None, None] if equips is None else equips,
            bourse=bourse,
            vitesse=vitesse,
            level=level,
            action=action,
            power=power,
            special=special,
        )
        self.action = 255

    def tir(self):
        theGame().hero.hp -= 2
        theGame().addMessage(f"Le Tireur vous tire dessus.", life=1)


class Pills(Element):
    "Pills are the game's money: we find them randomly in the game, they have a value according to their gold value."

    def __init__(
        self, name, abbvr=None, usage=None, transparent=True, pill_value=0
    ):
        Equipment.__init__(self, name, abbvr, usage, transparent)
        self.pill_value = pill_value

    def meet(self, creature: Creature):
        "Meet a pill: we add her value to our bourse."
        theGame().addMessage(f"Tu as ramassé des médicaments")
        creature.bourse += self.pill_value
        return True


class Equipment(Element):
    """Pickable Element.
    Could not be usable."""

    def __init__(
        self,
        name,
        abbvr=None,
        usage=None,
        transparent=True,
        enchant=[],
        f=False,
        used=None,
    ):
        Element.__init__(self, name, abbvr, transparent, f)
        self.usage = usage
        self.enchant = enchant
        self.used = used

    def meet(self, creature: Creature) -> True:
        "Meet a equipment: add him to the creature's equipment"
        a = creature.take(self)
        if a:
            theGame().addMessage(f"Tu as ramassé un{self.accord()}")
        else:
            theGame().addMessage(f"Mince, tu n'as plus de place!")
        return a

    def use(self, creature) -> bool:
        "Use an usable equipment"
        if self.usage != None:
            theGame().addMessage(f"The {creature.name} uses the {self.name}")
            return self.usage(creature)
        theGame().addMessage(f"The {self.name} is not usable")
        return False


class Edible(Equipment):
    def __init__(self, name, abbvr=None, miam=7, transparent=True, f=False):
        Equipment.__init__(self, name, abbvr, transparent=transparent, f=f)
        self.miam = miam

    def use(self, creature):
        """Feed the Hero with food elements"""
        creature.satiete += self.miam
        if isinstance(creature, Hero):
            creature.joie += 10
            creature.tristesse -= 10
            creature.colere -= 10
            creature.peur -= 10
        return True


class Used(Equipment):
    def __init__(self, name, abbrv="", usage=None):
        Equipment.__init__(self, name, abbrv, usage=None)

    def meet(self, creature):
        creature.action += 8
        print(creature.action)
        return True


class Enchant(object):
    "Enchant or upgrade to apply on an Equipment"

    def __init__(self, name="+", effect=None, increase=[("force", 1)]):
        self.name = name
        self.effect = effect
        self.increase = increase

    def appy(self, equip: Equipment):
        "Enchanting an Equipment: we increase the attributes targeted and add an effect, if necessary"
        equip.name += " " + self.name
        for i in self.increase:
            equip.__setitem__(i[0], i[1] + equip.__getitem__(i[0]))
            if self.effect != None:
                equip.enchant.append(self.effect)


class Hero(Creature):
    "The Hero, controled by the player in the game."

    def __init__(self, name="Hero", hp=37, abbrv="@", strength=2, satiete=100):
        Creature.__init__(self, name, hp, abbrv, strength,
                          distantstrenght=3, level=5)
        self.joie = 50
        self.tristesse = 50
        self.colere = 50
        self.peur = 50
        self.absp = 0
        self.satiete = satiete
        self.mp = 124323
        self.tour = 0
        self.famine = False
        self.distvision = 6

    def description(self) -> str:
        "Short description of the Hero."
        return Creature.description(self) + f"{self.inventory} ${self.bourse}"

    def __repr__(self) -> str:
        return self.abbrv

    def fullDescription(self) -> str:
        "Long description of the hero, including all his attributes"
        a = self.__dict__
        res = ""
        for i in a:
            if i[0] != "_":
                res += f"> {i} : {a[i]}\n"
        res += "> INVENTORY : " + str([x.name for x in self.inventory])
        return res

    def kill(self) -> None:
        "Function to kill the hero"
        self.hp = 0

    def use(self, item: Equipment) -> None:
        "Using an item: we use it with Equipment.use() and remove it from the Hero's inventory if necessary"
        if not (isinstance(item, Equipment)):
            print(item)
            raise TypeError("C'est pas un équipement!")
        if not (item in self.inventory):
            raise ValueError("Tu l'as pas, tu peux pas l'utiliser!")
        if item.use(self):
            self.inventory.remove(item)
            theGame().deselect()

    def useitem(self, number) -> None:
        [self.fenetre.bind(i, self.gameturn) for i in self._actions]
        self.use(self.inventory[number])

    def destroy(self, item: Union[str, Equipment]):
        if isinstance(item, str):
            for i in self.inventory:
                if i.name == item:
                    self.inventory.remove(i)
                    return True
        elif item in self.inventory:
            self.inventory.remove(item)

    def levelup(self) -> None:
        "Level up : stats are increased"
        self.hpmax += 5
        self.level += 1
        self.strength += 1
        self.joie += 20
        self.peur -= 20
        self.tristesse -= 20
        self.colere -= 20
        self.hp = self.hpmax
        theGame().addMessage(f"Bravo! Tu es maintenant niveau {self.level}")
        if self.level in theGame().sorts:
            theGame().addMessage(
                f"Tu as débloqué le {theGame().sorts[self.level]}!")

    def food(self) -> None:
        """The food level.
        Decreases every 3 turns, from 100 to 0.
        At 0, the hero loses hp each 3 turns."""
        self.tour += 1
        self.famine = (self.satiete <= 0)
        self.satiete = min(100, self.satiete)
        self.satiete = max(0, self.satiete)
        if self.tour % 3 == 0 and self.satiete > 0:
            self.satiete -= 1
        if self.tour % 3 == 0 and self.famine == True:
            self.heal(-1)
            theGame().addMessage("Il faut manger!", "red", 3)

    def sleep(self) -> None:
        listdpl = [
            Coord(0, -1),
            Coord(-1, -1),
            Coord(-1, 0),
            Coord(-1, 1),
            Coord(0, 1),
            Coord(1, 1),
            Coord(1, 0),
            Coord(1, -1),
        ]
        pos = theGame().floor.pos(self)
        for i in listdpl:
            if (
                isinstance(theGame().floor.get(pos + i), Element)
                and theGame().floor.get(pos + i).name == "lit"
            ):
                self.hp = min(self.hp + 5, self.hpmax)
                for _ in range(10):
                    theGame().gameturn("<space>")

    def emotion_effect(self) -> None:
        "Affects the hero according to its emotions"
        if self.tour % 5 == 0:
            # joie
            self.mp += int(self.joie / 10)
            self.heal(int(random.expovariate(1/((self.joie-50)/50))))
            if self.joie <= 10:
                self.hp -= 2
                self.tristesse += 1
                self.colere += 1
                self.peur += 5
            # tristesse
            self.distvision = 2.5 * (100-self.tristesse) / 100 + 2.5
            if self.tristesse <= 10:
                self.hp = min(self.hp + 2, self.hpmax)
                self.joie += 2
                self.peur -= 1
            elif self.tristesse <= 90:
                self.hp -= 1
            # peur
            if self.peur <= 10:
                self.hp += 2
                self.joie += 2
            elif self.peur <= 90:
                self.hp -= 1
                r = random.randint(1, 4)
                if r == 1:
                    theGame().gameturn("<space>")
                    self.peur += 2
            # colere
            if self.colere <= 10:
                self.hp += 2
                self.joie += 2


class Weapon(Equipment):
    "Equipable Equipment, increasing the creature's strength(Weapon: slot 0 in the Creature's equips)"

    def __init__(self, name, force, durabilite, abbrv="", usage=None, f=False):
        Equipment.__init__(self, name, abbrv, f=f, used="idem")
        self.usage = usage
        self.force = force
        self.durabilite = durabilite

    def equiper(self, creature: Creature) -> None:
        "Equipment of a weapon: we unequip the previous weapon,replace it by the new one, and increase the creature's strength."
        if creature.equips[0] != None:
            creature.equips[0].desequiper(creature)
        creature.strength += self.force
        creature.equips[0] = self

    def desequiper(self, creature: Creature) -> None:
        "Unequiping a Weapon: we decrease the creature's force and empty the slot"
        creature.equips[0] = None
        creature.strength -= self.force

    def use(self, creature: Creature) -> True:
        "Using a weapon: equip it and return True to remove it from the inventory."
        self.equiper(creature)
        return True


class Armor(Equipment):
    "Equipable Equipment, increasing the creature's defense(Armor: slot 1 in the Creature's equips)"

    def __init__(self, name, defense, durabilite, abbrv="", usage=None):
        Equipment.__init__(self, name, abbrv, used="idem")
        self.usage = usage
        self.defense = defense
        self.durabilite = durabilite

    def equiper(self, creature: Creature) -> None:
        "Equipment of a armor: we unequip the previous armor,replace it by the new one, and increase the creature's defense."
        if creature.equips[1] != None:
            creature.equips[1].desequiper(creature)
        creature.hp += self.defense
        creature.equips[1] = self

    def desequiper(self, creature: Creature) -> None:
        "Unequiping an Armor: we decrease the creature's defense and empty the slot"
        creature.hp -= self.defense
        creature.equips[1] = None

    def use(self, creature: Creature) -> True:
        "Using a armor: equip it and return True to remove it from the inventory."
        self.equiper(creature)
        return True


class Amulet(Equipment):
    "Equipable Equipment, increasing the hero's defense, strength, or other things if needed(Amulet: slot 2 in the Hero's equips)"

    def __init__(self, name, defense=0, force=0, courage=0, abbrv="", usage=None):
        Equipment.__init__(self, name, abbrv, used="idem")
        self.usage = usage
        self.defense = defense
        self.force = force
        self.courage = courage

    def equiper(self, creature: Hero) -> None:
        "Equipment of a amulet: we unequip the previous amulet,replace it by the new one, and increase the hero's stats."
        if creature.equips[2] != None:
            creature.equips[2].desequiper(creature)
        creature.hp += self.defense
        creature.strength += self.force
        creature.courage += self.courage
        creature.equips[2] = self

    def desequiper(self, creature: Hero) -> None:
        "Unequiping a Amulet: we decrease the hero's stats and empty the slot"
        creature.hp -= self.defense
        creature.strength -= self.force
        creature.courage -= self.courage
        creature.equips[2] = None

    def use(self, creature: Hero) -> True:
        "Using a amulet: equip it and return True to remove it from the inventory. Warning: only the Hero can equip an amulet!"
        if isinstance(creature, Hero):
            self.equiper(creature)
            return True
        raise TypeError("Not a Hero!")


class Coffre(Element):
    def __init__(self, name="coffre", abbrv="C"):
        Element.__init__(self, name, abbrv, transparent=True)

    def meet(self, creature: Creature):
        if "cle" in creature:
            creature.destroy("cle")
            coordcoffre = theGame().floor.pos(self)
            coordaround = theGame().floor.getcoordaround(coordcoffre, 3)
            theGame().floor.rm(coordcoffre)
            for object in [theGame().randEquipment() for _ in range(random.randint(1, 5))]:
                if len(coordaround) > 0:
                    inx = random.randint(0, len(coordaround))
                    print(coordaround[inx - 1])
                    theGame().floor.put(coordaround[inx - 1], object)
                    coordaround.pop(inx - 1)
            return theGame().addMessage("Vous avez ouvert le coffre", "blue", 5)
        return theGame().addMessage("Ce coffre ne s'ouvre qu'avec une clé..", "red", 3)


class NPC(Creature):
    "NPC creature, can talk when met."

    def __init__(self, name, hp=100, abbrv="", strength=0, defense=0, actif=None):
        Creature.__init__(self, name, hp, abbrv, strength, defense, actif)
        self.actif = actif

    def meet(self, other) -> None:
        "Adds dialogues in the messages."
        if isinstance(other, Hero):
            if self.actif != None:
                for i in self.actif:
                    theGame().addMessage(self.name + " : " + i)


class Seller(NPC):
    "Particular NPC that can sell you Equipments or Actions(<-not implemented yet)."

    def __init__(
        self,
        name="Infirmière",
        hp=100,
        abbrv="M",
        strength=0,
        defense=0,
        actif=[
            "Bonjour, mon loulou. Quel age as tu? Ah oui tu es jeune!",
            "Et qu'as tu dans tes poches? Si tu as trouvé des pillules bleus ou jaunes, ne les mange pas!",
            "Vient plutôt me les donner, en échange je te donnerai des cookies ou des sucreries.",
            "C'est d'accord?",
            "Alors, as tu trouvé ce type de médicaments?",
        ],
        dialoguenon=[
            "As tu trouvé des pillules au sol? Ce n'est pas grave loulou, reviens me voir si tu en trouves."
        ],
    ):
        NPC.__init__(self, name, hp, abbrv, strength, defense, actif)
        self.dialoguenon = dialoguenon
        self.chariot = []
        for i in range(3):
            self.chariot.append(theGame().randEquipmentM())

    def meet(self, creature) -> None:
        "Inits the dialogues and waits for the response with bind"
        if isinstance(creature, Hero):
            if theGame().hero.bourse <= 0:
                return self.fin_de_discussion()
            theGame().callseller(self)

            return True
            """'[theGame().addMessage(self.name+" : "+ i) for i in self.actif]
            theGame().fenetre.bind('b', self.fin_de_discussion())"""
        return False

    def fin_de_discussion(self) -> None:
        "Prints dialogs and exits"
        [theGame().addMessage(i) for i in self.dialoguenon]

    def achat(self, equipment):
        print("whtat")
        theGame().hero.bourse -= 3
        print(equipment)
        theGame().hero.inventory.append(equipment)


class Room():
    "Room defined by her corner's coord"

    def __init__(self, c1: Coord, c2: Coord):
        self.c1 = c1
        self.c2 = c2

    def __contains__(self, coord: Coord) -> bool:
        "Check if a Coord is in the Room"
        return self.c1.abs <= coord.abs <= self.c2.abs and self.c1.ord <= coord.ord <= self.c2.ord

    def __repr__(self) -> str:
        return f"[<{self.c1.abs},{self.c1.ord}>, <{self.c2.abs},{self.c2.ord}>]"

    def center(self) -> Coord:
        "Returns the center of the Room, using the Coord.middle method"
        return self.c1.middle(self.c2)

    def coins(self) -> List[Coord]:
        "Returns a list of all corners from the room"
        return [self.c1, self.c2, self.c1.coin1(self.c2), self.c2.coin1(self.c1)]

    def intersect(self, other) -> bool:
        "Checks if two rooms share Coords"
        for i in self.coins():
            if i in other:
                return True
        for i in other.coins():
            if i in self:
                return True
        return False

    def randCoord(self) -> Coord:
        "Returns a random Coord in the Room."
        return Coord(
            random.randint(self.c1.abs, self.c2.abs), random.randint(
                self.c1.ord, self.c2.ord)
        )

    def randEmptyCoord(self, map: "Floor") -> Coord:
        "Returns a coord not assigned to any Element in the Map"
        coord = self.center()
        cc = self.center()
        while (coord in map._creatures.values() or coord == cc) or not (
            map.get(coord) in Floor.listground
        ):
            print(coord)
            coord = self.randCoord()
        return coord

    def randEmptyCoord2(self, map: "Floor") -> Coord:
        "Returns a coord not assigned to any Element in the Map + the coord up from the previous one not assignated either"
        coord = self.center()
        cc = self.center()
        while (
            not (map.get(coord + Coord(0, -1)) in Floor.listground)
            or not (map.get(coord) in Floor.listground)
            or coord in map._creatures.values()
            or coord == cc
            or coord + Coord(0, -1) in map._creatures.values()
            or coord + Coord(0, -1) == cc
        ):
            coord = self.randCoord()
        return coord

    def decorate(self, map: "Floor", seller=True) -> None:
        "Adds random elements in the Room in the Map"
        map.put(self.randEmptyCoord(map), theGame().randEquipment())
        map.put(self.randEmptyCoord(map), theGame().randMonster())
        a = theGame().randDecoration()
        if len(a) == 1:
            map.put(self.randEmptyCoord(map), copy.copy(a[0]))
        elif len(a) == 2:
            c = self.randEmptyCoord2(map)
            for i in range(2):
                try:
                    map.put(c + Coord(0, -i), copy.copy(a[i]))
                except IndexError:
                    pass
        if seller == True:
            map.put(
                random.choice(map._rooms).randEmptyCoord(
                    map), theGame().randSeller()
            )


class SpeRoom(Room):
    "a triangular room in the map, has a size of 7 tiles."

    def __init__(self, c1, cent):
        self.c1 = c1
        self.c2 = Coord(self.c1.abs + 7, self.c1.ord)
        self.c3 = Coord((self.c1.abs + self.c2.abs) // 2, self.c1.ord + 4)
        self.mat = []
        for _ in range(4):
            self.mat.append([Floor.empty] * 7)
        index = 7 // 2
        taille_ligne = 1
        for y in range(len(self.mat) - 1, -1, -1):
            ligne = self.mat[y]
            for taille in range(taille_ligne):
                ligne[index + taille] = Floor.ground1
            taille_ligne += 2
            index -= 1

        self.cent = cent

    def __contains__(self, coord: Coord) -> bool:
        "Check if a Coord is in the Room"
        try:
            return self.mat[coord.ord - self.c1.ord][coord.abs - self.c1.abs] == Floor.ground1
        except IndexError:
            return False

    def __repr__(self) -> str:
        return f"[<{self.c1.abs},{self.c1.ord}>,<{self.c3.abs},{self.c3.ord}>, <{self.c2.abs},{self.c2.ord}>]"

    def center(self) -> Coord:
        "Returns the center of the Room, using the Coord.middle method"
        return self.c3.middle(self.c1.middle(self.c2))

    def coins(self) -> List[Coord]:
        "Returns a list of all corners from the room"
        return [self.c1, self.c2, self.c3]

    def intersect(self, other) -> bool:
        "Checks if two rooms share Coords"
        for i in self.coins():
            if i in other:
                return True
        for i in other.coins():
            if i in self:
                return True
        return False

    def randCoord(self) -> Coord:
        "Returns a random Coord in the Room."

        c = Coord(
            random.randint(self.c1.abs, self.c2.abs), random.randint(
                self.c1.ord, self.c3.ord)
        )
        print("generating eventually infinite loop...", end="")
        while not (c in self):
            c = Coord(
                random.randint(self.c1.abs, self.c2.abs),
                random.randint(self.c1.ord, self.c3.ord),
            )
            print(".", end="")
        print("done")
        return c

    def randEmptyCoord(self, map) -> Coord:
        "Returns a coord not assigned to any Element in the Map"
        coord = self.center()
        cc = self.center()
        while coord in map._creatures.values() or cc == coord:
            print(coord)
            coord = self.randCoord()
        return coord

    def decorate(self, map, seller=True, T="N") -> None:
        "Adds random elements in the Room in the Map"
        pass


class Attack():
    "An attack: basically a tile with an animation"

    def __init__(
        self, name, abbrv=None, dmg: int = 0, turns: int = 1, effects: List[Status] = []
    ) -> None:
        self.name = name
        self.abbrv = abbrv
        self.dmg = dmg
        self.effects = effects
        self.turns = turns

    def __repr__(self):
        return f"{self.name} <{self.turns} tours> *{self.dmg}"


class Floor():
    "Map of the Game, where Creatures live."
    ground1 = "."
    ground2 = ","
    ground3 = "`"
    ground4 = "´"
    listground = [ground1, ground2, ground3, ground4]
    groundwet1 = ".m"
    groundwet2 = ",m"
    groundwet3 = "`m"
    groundwet4 = "´m"
    wall = "|"
    listgroundwet = [groundwet1, groundwet2, groundwet3, groundwet4]
    listgrounds = listground+listgroundwet
    empty = " "

    def __init__(self, number_floor=1, size: int = None, nbrooms=10, menage=True, coffre=None):
        self.nbrooms = nbrooms
        self.size = constants.SIZEMAP if size is None else size
        self.number_floor = number_floor
        self._rooms = []
        self._roomsToReach = []
        self.menage = menage
        self._mat = [[self.empty for i in range(
            self.size)] for k in range(self.size)]
        self._creatures = {}
        self._attacks = {}
        self.generateRooms(self.nbrooms)
        if coffre == "O":
            self.generateSpeRoom(Coffre())
        self.reachAllRooms()
        self.generateEscalier()
        self.blankmap = [
            [str(self._mat[j][i]) for i in range(len(self))] for j in range(len(self))
        ]
        self.__len__ = (50, 50)
        self.put(self._rooms[0].center(), theGame().hero)
        for i in self._creatures.keys():
            self._mat[self._creatures.get(
                i).ord][self._creatures.get(i).abs] = i.abbrv
        for r in self._rooms:
            print(self)
            k = r.randEmptyCoord(self)
            if not (isinstance(r, SpeRoom)):
                r.decorate(self, r == self._rooms[1])
            else:
                self.put(k, r.cent)
        room = random.choice(self._rooms)
        while isinstance(room, SpeRoom):
            room = random.choice(self._rooms)
        if coffre == "O":
            c = room.randCoord()
            while self.get(c) in Floor.listground:
                c = room.randCoord()
            self.put(c, theGame().randMonsterKey(self))

    def __repr__(self) -> str:
        return (
            "\n".join(
                [
                    "".join([str(self._mat[n][k]) for k in range(len(self))])
                    for n in range(len(self))
                ]
            )
            + "\n"
        )

    def __len__(self) -> int:
        "Returns the len of the tiles matrix, since the Map is a square"
        return len(self._mat)

    def __contains__(self, item) -> bool:
        "Check, for an element, if it is in _creatures, or for a coord, if it is in the map"
        if isinstance(item, Coord):
            return 0 <= item.abs <= len(self) - 1 and 0 <= item.ord <= len(self) - 1
        return item in self._creatures.keys()

    def containsmieux(self, c: Coord) -> bool:
        for val in c:
            if val > self.size:
                return False
        return True

    def __getitem__(self, item) -> Union[Coord, Element]:
        "Returns, for an Element, its Coord in the map, and for a Coord, its Element. Counts the number of times it is called"
        if type(item) is Coord:
            return self.get(item)
        else:
            return self.pos(item)

    def __setitem__(self, cle, valeur) -> None:
        "Moves or adds elements to the given Coord."
        if type(cle) is Coord:
            self.put(cle, valeur)
        else:
            if not cle in self:
                self.put(valeur, cle)
            else:
                self.tp(cle, valeur)

    def getattacks(self):
        return self._attacks

    def getrooms(self):
        return self._rooms[:]

    def get(self, coord: Coord, testeroupas=True) -> Element:
        "Returns the Element in the Map having this Coord."
        if testeroupas:
            self.checkCoord(coord)
        for i, j in self._creatures.items():
            if j == coord:
                return i
        return self._mat[coord.ord][coord.abs]

    def pos(self, element: Element) -> Coord:
        "Returns the Coords of an Element"
        self.checkElement(element)
        return self._creatures.get(element)

    def groundize(self, coord: Coord) -> None:
        "Puts a ground on a cell.(we have 4 different grounds, and they are saved in blankmap)"
        self._mat[coord.ord][coord.abs] = self.blankmap[coord.ord][coord.abs]

    def elementize(self, coord: Coord, abbrv: str) -> None:
        "Puts the abbvr of an Element on the Map."
        self._mat[coord.ord][coord.abs] = abbrv

    def put(self, coord: Coord, element: Element) -> None:
        "Puts an Element at the given Coord."
        if type(coord) is type(None) or type(element) is type(None):
            return
        self.checkCoord(coord)
        self.checkElement(element)
        if (
            self[coord] == self.empty
            or (isinstance(self[coord], Element))
            or (isinstance(self[coord], Special_ground))
        ):
            print(f"#{self[coord]}#")
            raise ValueError("Incorrect cell")
        if element in self:
            raise KeyError("Already placed")
        self._creatures[element] = Coord(coord.abs, coord.ord)
        self.elementize(coord, element.abbrv)

    def putattack(self, coord: Coord, attack: Attack) -> None:
        "Puts an Attack at the given Coord."
        if type(coord) is type(None) or type(attack) is type(None):
            return
        self.checkCoord(coord)
        for i in self._attacks:
            if self._attacks[i] == coord and i.name == attack.name:
                print("pasbon" + str(coord))
                return
        self._attacks[copy.copy(attack)] = Coord(coord.abs, coord.ord)

    def rm(self, object: Union[Element, Coord]) -> None:
        "Removes the Element from the Map(or the element at the given Coord)"
        coordarr = self.pos(object) if isinstance(object, Element) else object
        if type(object) is Coord:
            self.checkCoord(object)
            self._creatures = {key: val for key,
                               val in self._creatures.items() if not val == object}
            self.groundize(object)
        else:
            self.groundize(self.pos(self._creatures.pop(object)))
        if isinstance(object, Creature):
            for ele in object.inventory:
                theGame().floor.put(coordarr, ele)

    def move(self, creature: Creature, way: Coord) -> None:
        "Moves an element from a Coord to another relatively, meets the destination."
        coordarr = self.pos(creature) + way
        if isinstance(creature, Creature):
            creature.facing = way
        if isinstance(creature, Hero):
            creature.abbrv = "@"
        if coordarr in self or (self[coordarr] == self.empty and isinstance(creature, Flying)):
            if not coordarr in self._creatures.values() and (
                self._mat[coordarr.ord][coordarr.abs] in Floor.listground
                or self._mat[coordarr.ord][coordarr.abs] in Floor.listgroundwet
            ):
                if self._mat[coordarr.ord][coordarr.abs] in Floor.listgroundwet:
                    Special_ground.glissade(self, creature)
                self.groundize(self.pos(creature))
                self._creatures[creature] = coordarr
                self.elementize(coordarr, creature.abbrv)
            elif self._mat[coordarr.ord][coordarr.abs] != Floor.empty:
                a = self.get(coordarr)
                if a.meet(creature):
                    self.rm(coordarr)

    def getcoordaround(self, index: Coord, radius: int):
        "returns the list of the coords of all the free cells around the index"
        output = []
        for y in range(index.ord - radius, index.ord + radius):
            for x in range(index.abs - radius, index.abs + radius):
                if Coord(x, y) in self and self.get(Coord(x, y)) in self.listgrounds:
                    output.append(Coord(x, y))
        return output

    def tp(self, element: Element, dest: Coord) -> None:
        "Moves absolutely"
        self.move(element, self.pos(element) - dest)

    def attackpoison(self, coord: Coord) -> None:
        if theGame().hero.level >= constants.LEVEL_POISON and theGame().hero.mp >= constants.MP_POISON:
            theGame().hero.mp -= constants.MP_POISON
            self.putattack(
                coord, Attack("Poison", "psn", 0, 10, [
                              Status("Poison", 5, -3, prb=1)])
            )
            theGame().addMessage("Sort de poison activé!", "blue", 1)
        elif theGame().hero.level < 2:
            theGame().addMessage("Tu n'as pas le niveau requis pour utiliser ce sort! Niveau requis: " +
                                 str(constants.LEVEL_POISON))
        else:
            theGame().addMessage(
                f"Tu n'as pas assez de MP pour utiliser ce sort! Tu en as {theGame().hero.mp}/{constants.MP_POISON}")

    def attackwind(self, coord: Coord) -> None:
        if theGame().hero.level >= 3 and theGame().hero.mp >= 7:
            theGame().hero.mp -= 7
            for direction in theGame().directions:
                self.putattack(
                    coord+direction, Attack("Wind", "wnd", -10, 5, []))
            theGame().addMessage("Sort de vent activé!", "blue", 1)
        elif theGame().hero.level < 3:
            theGame().addMessage("Tu n'as pas le niveau requis pour utiliser ce sort! Niveau requis: 3")
        else:
            theGame().addMessage(
                f"Tu n'as pas assez de MP pour utiliser ce sort! Tu en as {theGame().hero.mp}/7")

    def attackfire(self, coord: Coord, facing: Coord) -> None:
        if theGame().hero.level >= 4 and theGame().hero.mp >= 10:
            theGame().hero.mp -= 10
            theta = facing.getangle() - math.pi / 12
            ch = coord
            while theta <= facing.getangle() + math.pi / 12:
                r = 1
                cv = Coord(0, 0)
                while (
                    r <= theGame().hero.distvision
                    and (ch + cv in self)
                    and (
                        (self[ch + cv] in Floor.listgrounds)
                        or (
                            isinstance(self[ch + cv], Element)
                            and self[ch + cv].transparent == True
                        )
                    )
                ):
                    self.putattack(
                        cv + ch,
                        Attack("Feu", "feu", -5, 10, [
                               Status("Brulé", 5, -1, prb=1)]),
                    )
                    r += 0.2
                    cv = Coord(r, theta, True)
                cv = Coord(r + 0.5, theta, True)
                if r < 6 and ch + cv in self:
                    self.putattack(
                        cv + ch,
                        Attack("Feu", "feu", 5, 10, [
                               Status("Brulé", 5, -1, prb=1)]),
                    )
                theta += math.pi / 32
            theGame().addMessage("Sort de feu activé!", "blue", 1)
        elif theGame().hero.level < 2:
            theGame().addMessage("Tu n'as pas le niveau requis pour utiliser ce sort! Niveau requis: 4")
        else:
            theGame().addMessage(
                f"Tu n'as pas assez de MP pour utiliser ce sort! Tu en as {theGame().hero.mp}/10")

    def wallline(self, c1: Coord, c2: Coord):
        """puts walls(using randwall) in the horizontal line between c1 and c2"""
        if c1.abs > c2.abs:
            c1, c2 = c2, c1
        for x in range(c1.abs, c2.abs+1):
            self.putWall(Coord(x, c1.ord))

    def randWall(self) -> str:
        "Returns a copy from an element of a dictionnary in the form {rarity<int> : List[Element],...}"
        x = random.expovariate(1 / self.number_floor)
        n = int(x)
        collection = theGame().walls
        while not (n in collection):
            n -= 1
        return random.choice(collection[n])

    def putWall(self, coord: Coord) -> None:
        "puts a wall at the coord"
        if coord in self:
            self._mat[coord.ord][coord.abs] = self.randWall()

    def fillrectangle(self, c1: Coord, c2: Coord, thing=empty) -> None:
        "Fills a rectangle of Coords with a given object. For a list, the object will be chosen randomly"
        for i in range(c1.abs, c2.abs + 1):
            for j in range(c1.ord, c2.ord + 1):
                try:
                    self._mat[j][i] = thing if type(
                        thing) is str else random.choice(thing)
                except IndexError:
                    print(f"{Coord(i,j)} not in the map")

    def filltriangle(self, room: SpeRoom) -> None:
        for y in range(room.c1.ord, room.c3.ord):
            for x in range(room.c1.abs, room.c2.abs):
                self._mat[y][x] = room.mat[y - room.c1.ord][x - room.c1.abs]

    def addRoom(self, room: Room) -> None:
        "Adds a Room to the list of rooms to reach, and fills the Map with grounds"
        self._roomsToReach.append(room)
        if isinstance(room, SpeRoom):
            self.filltriangle(room)
        else:
            # self.fillrectangle(room.c1+Coord(-1, 1),
            #                    room.c2+Coord(1, 1), Floor.wall)
            self.fillrectangle(room.c1, room.c2, Floor.listground)
            self.wallline(room.c1+Coord(0, -1), room.c2+Coord(0, -1))

    def findRoom(self, coord: Coord) -> Any:
        "Finds the first Room of the map containing the Coord, returns False if none."
        for i in self._roomsToReach:
            if coord in i:
                return i
        return False

    def intersectNone(self, room: Room) -> bool:
        "Check if any Room on the Map intersects the one we're checking"
        for i in self._roomsToReach:
            if room.intersect(i):
                return False
        return True

    def dig(self, coord: Coord) -> None:
        "Groundizes a Coord, and if it is in a room, removes it from roomToReach."
        alea = random.randint(1, 10)
        if alea == 3 and self.menage == True:
            self._mat[coord.ord][coord.abs] = random.choice(self.listgroundwet)
        else:
            self._mat[coord.ord][coord.abs] = random.choice(self.listground)
        a = self.findRoom(coord)
        if a:
            self._rooms.append(a)
            self._roomsToReach.remove(a)

    def corridor(self, c1: Coord, c2: Coord) -> None:
        "Digs from a Coord to another"
        self.dig(c1)
        coord = Coord(c1.abs, c1.ord)
        while not (coord == c2):
            coord += self.dircorridor(coord, c2)
            self.dig(coord)

    def dircorridor(self, c1: Coord, c2: Coord) -> Coord:
        "Returns the direction to dig to."
        if c1.ord != c2.ord:
            return Coord(0, 1) if c1.ord < c2.ord else Coord(0, -1)
        if c1.abs != c2.abs:
            return Coord(1, 0) if c1.abs < c2.abs else Coord(-1, 0)

    def reach(self) -> None:
        "Digs between two random rooms."
        r1 = random.choice(self._rooms)
        r2 = random.choice(self._roomsToReach)
        self.corridor(r1.center(), r2.center())

    def reachAllRooms(self) -> None:
        "Reachs all rooms of the Map."
        self._rooms.append(self._roomsToReach.pop(0))
        while len(self._roomsToReach) > 0:
            self.reach()

    def randRoom(self) -> Room:
        "Creates a random room"
        x1 = random.randint(3, len(self) - 7)
        y1 = random.randint(3, len(self) - 7)
        largeur = random.randint(4, 8)
        hauteur = random.randint(4, 8)
        x2 = min(len(self) - 1, x1 + largeur)
        y2 = min(len(self) - 1, y1 + hauteur)
        return Room(Coord(x1, y1), Coord(x2, y2))

    def randSpeRoom(self, cent) -> SpeRoom:
        x1 = random.randint(0, len(self) - 7)
        y1 = random.randint(0, len(self) - 7)
        return SpeRoom(Coord(x1, y1), cent)

    def generateRooms(self, n) -> None:
        "Creates n Rooms, and if possible, adds them to the Map (-> puts from 0 to n new Rooms)"
        for i in range(n):
            r = self.randRoom()
            if self.intersectNone(r):
                self.addRoom(r)

    def generateSpeRoom(self, cent):
        l = len(self._roomsToReach)
        while len(self._roomsToReach) == l:
            r = self.randSpeRoom(cent)
            if self.intersectNone(r):
                self.addRoom(r)

    def generateEscalier(self):
        c = random.choice(theGame().directions)
        self.put((self._rooms[0].center() + c), Stairs("Monter", ">", up=True))
        salle_down = random.choice(self._rooms)
        while salle_down == self._rooms[0] or isinstance(salle_down, SpeRoom):
            salle_down = random.choice(self._rooms)
        c = random.choice(theGame().directions)
        self.put(salle_down.center() + c, Stairs("Descendre", "<", up=False))

    def randWall(self) -> str:
        "Returns a copy from an element of a dictionnary in the form {rarity<int> : List[Element],...}"
        x = random.expovariate(1 / self.number_floor)
        n = int(x)
        collection = theGame().walls
        while not (n in collection):
            n -= 1
        return random.choice(collection[n])

    def moveAllMonsters(self) -> None:
        """Moves all creatures from the map, except the Hero."""
        for i in self._creatures:
            if isinstance(i, Creature) and not (
                isinstance(i, Hero) or isinstance(i, NPC)
            ):
                i.creaturn(self)
                if i.action > 0:
                    i.action -= 1
                    if isinstance(i, Archer):
                        if self._creatures[i].distance(self._creatures[theGame().hero]) < 3:
                            Archer.tir(self)
                    pass
                else:
                    for _ in range(i.vitesse):
                        if self._creatures[i].distance(self._creatures[theGame().hero]) <= 1 or (
                            (
                                self._creatures[i].cosinus(
                                    self._creatures[theGame().hero])
                                == (1 / math.sqrt(2) or -1 / math.sqrt(2))
                            )
                            and self._creatures[i].distance(self._creatures[theGame().hero])
                            <= math.sqrt(2)
                        ):
                            theGame().hero.meet(i)
                        elif self._creatures[i].distance(self._creatures[theGame().hero]) < 6:
                            posmonstre = self.pos(i)
                            poshero = self.pos(theGame().hero)
                            new = posmonstre - poshero
                            way1 = Coord(-utils.sign(new.abs), -
                                         utils.sign(new.ord))
                            # diagonale 'imparfaite'
                            if ((way1.abs and way1.ord) != 0) and (
                                self._creatures[i].cosinus(
                                    self._creatures[theGame().hero])
                                != (1 / math.sqrt(2) or -1 / math.sqrt(2))
                            ):
                                way2 = self._creatures[i].direction(
                                    self._creatures[theGame().hero])
                                # creation de way3 et way4
                                if way2.ord == 0:
                                    way3 = Coord(way2.abs, -way1.ord)
                                    way4 = Coord(0, way1.ord)
                                else:
                                    way3 = Coord(-way1.abs, way2.ord)
                                    way4 = Coord(way1.abs, 0)
                                way5 = 0
                            # diagonales 'parfaites'
                            elif (way1.abs and way1.ord) != 0:
                                # creation de way2, way3, way4, way5
                                way2 = Coord(0, way1.ord)
                                way3 = Coord(way1.abs, 0)
                                way4 = Coord(way1.abs, -way1.ord)
                                way5 = Coord(-way1.abs, way1.ord)

                            # cas ou le monstre doit se deplacer en ligne droite
                            else:
                                if way1.abs == 0:
                                    way2 = Coord(1, way1.ord)
                                    way3 = Coord(-1, way1.ord)
                                    way4 = Coord(1, 0)
                                    way5 = Coord(-1, 0)
                                else:
                                    way2 = Coord(way1.abs, 1)
                                    way3 = Coord(way1.abs, -1)
                                    way4 = Coord(0, 1)
                                    way5 = Coord(0, -1)

                            # cas ou il n'y a aucun obstacle devant la premiere direction (on privilegie le deplacement en diagonale)
                            if (
                                (self._creatures[i] + way1) in self
                                and (
                                    self.get(
                                        self._creatures[i] + way1) in self.listground
                                    or self.get(self._creatures[i] + way1)
                                    in self.listgroundwet
                                )
                                or isinstance(self.get(self._creatures[i] + way1), Used)
                            ):
                                self.move(i, way1)

                            # cas ou il y a un obstacle devant la premiere direction possible, on choisi donc la deuxieme direction possible
                            elif (
                                (self._creatures[i] + way2) in self
                                and (
                                    self.get(
                                        self._creatures[i] + way2) in self.listground
                                    or self.get(self._creatures[i] + way2)
                                    in self.listgroundwet
                                )
                                or isinstance(self.get(self._creatures[i] + way2), Used)
                            ):
                                self.move(i, way2)

                            # cas ou il y a un obstacle devant la premiere et deuxieme direction possible, on choisi donc la troisieme direction possible
                            elif (
                                (self._creatures[i] + way3) in self
                                and (
                                    self.get(
                                        self._creatures[i] + way3) in self.listground
                                    or self.get(self._creatures[i] + way3)
                                    in self.listgroundwet
                                )
                                or isinstance(self.get(self._creatures[i] + way3), Used)
                            ):
                                self.move(i, way3)

                            # cas ou il y a un obstacle devant la premiere, deuxieme et troisieme direction possible, on choisi donc la quatrieme direction possible
                            elif (
                                (self._creatures[i] + way4) in self
                                and (
                                    self.get(
                                        self._creatures[i] + way4) in self.listground
                                    or self.get(self._creatures[i] + way4)
                                    in self.listgroundwet
                                )
                                or isinstance(self.get(self._creatures[i] + way4), Used)
                            ):
                                self.move(i, way4)

                            # cas ou il y a un obstacle devant la premiere, deuxieme ,troisieme et quatrieme direction possible, on choisi donc la cinquieme direction possible
                            elif (
                                (self._creatures[i] + way5) in self
                                and (
                                    self.get(
                                        self._creatures[i] + way5) in self.listground
                                    or self.get(self._creatures[i] + way5)
                                    in self.listgroundwet
                                )
                                or isinstance(self.get(self._creatures[i] + way5), Used)
                            ) and isinstance(way5, Coord):
                                self.move(i, way5)

    def checkCoord(self, coord) -> None:
        "Method to check if an object is a Coord in the Map. Raises errors."
        if not (type(coord) is Coord):
            raise TypeError("Not a Coord")
        if not coord in self:
            raise IndexError("Out of map coord")

    def checkElement(self, elem) -> None:
        "Method to check if an object is an Element. Raises errors."
        if not (isinstance(elem, Element)) and not (isinstance(elem, Special_ground)):
            raise TypeError("Not a Element")

    def turn(self):
        newattack = {}
        for i in self._attacks:
            i.turns -= 1
            if i.turns >= 0:
                newattack[i] = self._attacks[i]
        self._attacks = newattack

    def getrooms(self):
        return self._rooms[:]


class Special_ground():
    "Special ground affecting the hero"

    def __init__(self, name, abbrv="#", effect=None):
        self.name = name
        self.abbrv = abbrv
        self.effect = effect

    def __repr__(self) -> str:
        return self.abbrv

    def glissade(self, creature):
        alea = random.randint(1, 5)
        if alea == 3:
            creature.hp -= 1
            if isinstance(creature, Hero):
                creature.abbrv = "@*"
                creature.colere += 1
                creature.tristesse += 1
            theGame().addMessage(
                f"{str(creature)} glisse sur le sol mouillé."
            )


class Stairs(Special_ground):
    "Stairs allowing the Hero to change the stage he plays in."

    def __init__(self, name, abbrv="#", effect=True, up=False):
        Special_ground.__init__(self, name, abbrv, effect)
        self.up = up

    def meet(self, hero):
        "Changes the stage where the Hero is."
        if isinstance(hero, Hero):
            if self.up == True:
                if theGame().stage == theGame().first_stage:
                    return
                print("MONTE")
                theGame().addMessage(
                    f"{hero.name} prend les escaliers et monte à l'étage {theGame().stage + 1}.")
                theGame().stage = theGame().stage + 1
                theGame().floor = theGame().etages[theGame().stage]
                theGame().seenmap = [
                    [Floor.empty for i in range(theGame().sizemap + 2)]
                    for k in range(theGame().sizemap + 2)
                ]

            else:
                print("DESCEND")
                theGame().addMessage(
                    f"{hero.name} prend les escaliers et descend à l'étage {theGame().stage - 1}.")
                print(theGame().stage)
                theGame().stage = theGame().stage - 1
                theGame().floor = theGame().etages[theGame().stage]
                theGame().seenmap = [
                    [Floor.empty for i in range(theGame().sizemap + 2)]
                    for k in range(theGame().sizemap + 2)
                ]


class Game():
    """The Game class.
        \nPlease use theGame() to remain in the same game..."""

    _actions = {
        "esc": lambda _: theGame().quit(),
        "z": lambda _: theGame().floor.move(theGame().hero, Coord(0, -1)),
        "a": lambda _: theGame().floor.move(theGame().hero, Coord(-1, -1)),
        "q": lambda _: theGame().floor.move(theGame().hero, Coord(-1, 0)),
        "w": lambda _: theGame().floor.move(theGame().hero, Coord(-1, 1)),
        "x": lambda _: theGame().floor.move(theGame().hero, Coord(0, 1)),
        "c": lambda _: theGame().floor.move(theGame().hero, Coord(1, 1)),
        "d": lambda _: theGame().floor.move(theGame().hero, Coord(1, 0)),
        "e": lambda _: theGame().floor.move(theGame().hero, Coord(1, -1)),
        "i": lambda _: theGame().addMessage(theGame().hero.fullDescription()),
        "r": lambda _: theGame().hero.sleep(),
        "1": lambda _: theGame().floor.attackpoison(
            theGame()[theGame().hero]+theGame().hero.facing
        ),
        "2": lambda _: theGame().floor.attackwind(theGame()[theGame().hero]),
        "3": lambda _: theGame().floor.attackfire(
            theGame().floor.pos(theGame().hero), theGame().hero.facing
        ),
        "k": lambda _: theGame().hero.kill(),
        "<space>": lambda _: theGame().tour(),
        "u": lambda _: theGame().select(theGame().hero.inventory),
        "j": lambda _: theGame().hero.throw(theGame().select(theGame().hero.inventory)),
        "<Escape>": lambda _: theGame().fenetre.destroy,
    }
    walls = {0: ["|1", "|2"], 1: ["|3"], 3: ["|4"]}
    monsters = {
        0: [
            # Creature("Sad emotivo", 4, "G"),
            Creature("Fear emotivo", 2, "W", vitesse=2),
        ],
        1: [
            Creature("Angry emotivo", 6, "O", strength=2),
            Creature("Ourson", 10, "B"),
            Creature("Araignée", 2, "Ar", strength=0,
                     power=Status("Poison", 5, -1)),
            Creature(
                "Fantome", 4, "fi", special=lambda creature: creature.unhide("fv")
            ),
            Archer("Tireur", 4, "T"),
        ],
        3: [
            NPC(
                "Docteur",
                abbrv="docM",
                strength=0,
                defense=0,
                actif=[
                    "Tes parents t’attendent en bas. Fais attention, le ménage a été fait, le sol peut être glissant par endroits"
                ],
            ),
            NPC(
                "Docteur",
                abbrv="docF",
                strength=0,
                defense=0,
                actif=[
                    "Si tu as une quelconque question, appuie sur <i> tu auras surement ta réponse."
                ],
            ),
            NPC(
                "Infirmière",
                abbrv="inf",
                strength=0,
                defense=0,
                actif=[
                    "Wow, tu deviens un grand tu sais! Mon conseil : ne fuis pas trop tes émotions ! Tu as de grandes poches ! Tu peux utiliser les objets dedans en appuyant sur <U>."
                ],
            ),
        ],
        5: [Creature("Boulimie", 20, strength=3)],
    }
    equipments = {
        0: [
            Weapon("épée", 3, 37, "s", f=True),
            Equipment(
                "gum",
                "g",
                usage=lambda creature: creature.trow(True),
                used=Used("used chewing-gum", "u"),
            ),
            Equipment("potion", "!",
                      usage=lambda creature: creature.heal(3), f=True),
            Pills("or1", "b", pill_value=1),
            Edible(
                "sucette baveuse",
                "s3",
                5,
                f=True,
            ),
        ],
        1: [
            Equipment("lance-pierre", "a",
                      usage=lambda creature: creature.tir()),
            Pills("or2", "j", pill_value=2),
            Edible(
                "sucette croquée",
                "s2",
                15,
                f=True,
            ),
        ],
        2: [
            Armor("plaid", 5, 5, "pl"),
            Pills("or5", "p", pill_value=5),
            Edible(
                "sucette",
                "s1",
                35,
                f=True,
            ),
            Edible(
                "cookie choco",
                "cc",
                40,
            ),
            Edible("happy pills", "HP", 50),
        ],
        3: [
            Pills("or10", "J", pill_value=10),
            Amulet("carte de docteur", defense=5,
                   force=5, courage=5, abbrv="Cd"),
            Amulet("foulard", defense=10, force=2,
                   courage=15, abbrv="foulard"),
            Armor("plaid", 5, 5, "pl"),
        ],
    }
    marchande = {
        0: [
            Weapon("épée", 3, 37, "s", f=True),
            Equipment(
                "gum",
                "g",
                usage=lambda creature: creature.throw(True),
                used=Used("used chewing-gum", "u"),
            ),
            Equipment("potion", "!",
                      usage=lambda creature: creature.heal(3), f=True),
        ],
        1: [
            Equipment("lance-pierre", "a",
                      usage=lambda creature: creature.tir()),
            Edible(
                "cookie choco",
                "cc",
                40,
            ),
            Edible("sucette", "s3", 35),
        ],
        2: [Armor("plaid", 5, 5, "pl")],
    }
    decorations = {
        0: [
            [Decoration("lit", "Be2", True), Decoration("lit", "Be1", True)],
            [Decoration("fauteuil", "Fa", True)],
            [Decoration("pot", "Po", True)],
            [Decoration("trou", "Tr", True)],
        ]
    }
    directions = [
        Coord(0, 1),
        Coord(1, 1),
        Coord(1, 0),
        Coord(1, -1),
        Coord(0, -1),
        Coord(-1, -1),
        Coord(-1, 0),
        Coord(-1, 1),
    ]
    sorts = {2: "sort de poison", 3: "sort de vent", 4: "sort de feu"}

    def __init__(self, sizemap=50, stage=10):
        self.hero = Hero()
        self.floor = None
        self._message = []
        self.seenmap = [
            [Floor.empty for i in range(sizemap + 2)] for k in range(sizemap + 2)
        ]
        self.sizemap = sizemap
        self.viewablemap = [
            [Floor.empty for i in range(self.sizemap + 2)]
            for k in range(self.sizemap + 2)
        ]
        self.stage = stage
        self.first_stage = self.stage
        self.etages = []
        self.level = self.first_stage - self.stage + 1
        self.buttons = []

    def __getitem__(self, key):
        return self.floor[key]

    def __setitem__(self, key, value):
        self.floor[key] = value

    def buildFloor(self) -> None:
        "Creates the Game's floor."
        for i in range(11):
            self.etages.append(
                Floor(
                    self.sizemap,
                    nbrooms=int(self.sizemap / 5),
                    coffre="O" if i % 2 else None,
                )
            )
        self.floor = self.etages[-1]

    def addMessage(self, msg: str, color="yellow", life=3) -> None:
        "Adds a message to be printed on the screen."

        self._message.append(
            [msg if msg[-1] in constants.PONCT else msg + ".", color, life])
        print(msg)

    def readMessages(self) -> str:
        "Yields all messages to be printed on the screen"
        for i in self._message:
            i[2] -= 1
            print(i)
            yield i
        # n=0
        # while n<len(self._message):
        #     if self._message[n][2]<=0:
        #         del self._message[n]
        #     else:
        #         n+=1
        self._message = [
            self._message[n] for (n, [_, _, i]) in enumerate(self._message) if i > 0
        ]

    def randElement(self, collection: dict) -> Element:
        "Returns a copy from an element of a dictionnary in the form {rarity<int> : List[Element],...}"
        x = random.expovariate(1 / self.level)
        n = int(x)
        while not (n in collection):
            n -= 1
        return copy.copy(random.choice(collection[n]))

    def randEquipment(self) -> Equipment:
        "Returns a random Equipment using randElement"
        return self.randElement(self.equipments)

    def randEquipmentM(self) -> Equipment:
        "Returns a random Equipment using randElement"
        return self.randElement(self.marchande)

    def randMonster(self) -> Creature:
        "Returns a random Creature using randElement"
        return self.randElement(self.monsters)

    def randMonsterKey(self, map: "Floor") -> None:
        """Gives a key to a random monster and adds it to the map."""
        monster = self.randMonster()
        r = random.choice(map._rooms)
        c = r.randEmptyCoord(map)
        monster.inventory.append(Equipment("cle", "cle", used="idem"))
        map.put(c, monster)

    def randDecoration(self) -> List[Decoration]:
        "Returns a random Equipment using randElement"
        return self.randElement(self.decorations)

    def randSeller(self):
        return Seller()

    def select(self, list_equips: List[Equipment], jeter=False):
        """Creates buttons to choose which Equipment to use."""
        for i in list_equips:
            # if jeter:
            self.buttons.append(
                tkinter.Button(
                    self.fenetre,
                    text=i.name,
                    bg="steel blue",
                    fg="cyan",
                    font=("Comic Sans MS", 10),
                    command=lambda z=i: theGame().hero.throw(
                        z) if jeter else theGame().hero.use(z),
                )
            )
            # else:
            #     self.buttons.append(
            #         tkinter.Button(
            #             self.fenetre,
            #             text=i.name,
            #             bg="steel blue",
            #             fg="cyan",
            #             font=("Comic Sans MS", 10),
            #             command=lambda z=i: theGame().hero.use(z),
            #         )
            #     )
        for index, button in enumerate(self.buttons):
            button.place(x=355, y=38 + 79 * index)

    def deselect(self):
        """Erase inventory buttons"""
        print(self.buttons)
        for i in self.buttons:
            i.destroy()
        self.buttons = []

    def initgraph(self) -> None:
        "Creates the dictionary of images,and binds actions to the Tk window, then creates the mainloop."
        self.canvas.config(width=1000, height=800)
        self.dicimages, self.dicanim, self.dicappear, self.dicequipement, self.dicinventory, self.dicinventoryM, self.dicseen, self.dicviewable, self.dicatk, self.dicemotion, self.dicother = images.get_dictionaries()
        self.seeMap()
        self.updategraph()
        [self.fenetre.bind(i, self.gameturn) for i in self._actions]
        self.canvas.pack()
        self.fenetre.mainloop()

    def gameturn(self, event) -> None:
        "Makes an action according to the bind result"
        poshero = self.floor.pos(self.hero)
        if isinstance(event, tkinter.Event) and event.char in self._actions:
            self._actions[event.char](theGame().hero)
        [self.fenetre.bind(i, None) for i in self._actions]
        self.hero.food()
        self.hero.creaturn(self.floor)
        if self.hero.tour % 7 == 0:
            self.hero.emotion_effect()
        self.floor.moveAllMonsters()
        self.floor.turn()
        self.seeMap()
        for i in range(3):
            print("TURN")
            self.updategraph(i, [self.floor.pos(self.hero), poshero], i == 2)
            print(poshero, self.floor.pos(self.hero))
            time.sleep(constants.DELAIANIM)
        [self.fenetre.bind(i, self.gameturn) for i in self._actions]

    def makeAction(self, action: str) -> None:
        "Makes an action"
        print(action)
        self._actions[action](theGame().hero)

    def callseller(self, seller):
        self.canvas.create_image(400, 500, image=self.dicother["black"])
        self.canvas.create_image(
            400, 500, image=self.dicother["marchandepage"])
        place = 0
        for i in range(len(seller.chariot)):
            picture = self.dicinventoryM.get(seller.chariot[i].abbrv)
            self.canvas.create_image(300 + 150 * place, 590, image=picture)
            self.canvas.create_text(
                300 + 100 * place, 540, text=seller.chariot[i].name)
            place = place + 1
        self.fenetre.bind(i - 1, seller.achat(copy.copy(seller.chariot[i])))
        self.canvas.pack()
        self.fenetre.mainloop()

    def updategraph(self, n=0, position=None, last=False) -> None:
        """Main graphic function.
        Displays the map on the canvas, using the images defined in initgraph.
        Then adds the minimap on the corner of the screen (place not defined yet, currently (650,800)).
        And ends the game if the Hero is dead."""
        y = 0
        self.canvas.delete("all")
        print(
            self.floor,
            "\n".join(
                [
                    "".join([str(self.viewablemap[n][k])
                            for k in range(self.sizemap)])
                    for n in range(self.sizemap)
                ]
            )
            + "\n",
        )  # -> debug
        if position == None:
            poshero = self.floor.pos(self.hero)
        else:
            poshero = (position[1] - position[0]) * -(n + 1 - 3)
            poshero = Coord(
                poshero.abs / 3 + position[0].abs,
                poshero.ord / 3 + position[0].ord,
                broken=True,
            )
            if position[0] == position[1]:
                n = 2
        for i in self.viewablemap:
            x = 0
            for k in i:
                if k != Floor.empty:
                    self.canvas.create_image(
                        ((Coord(x, y) - poshero) * 64 + Coord(401, 400)).ind(),
                        image=self.dicimages.get(
                            self.floor.blankmap[int(y)][int(x)]),
                    )
                x += 1
            y += 1
        y = 0
        for i in self.viewablemap:
            x = 0
            for k in i:
                if k in self.dicimages and not (
                    k in Floor.listground or k in Floor.listgroundwet
                ):
                    imagecase = self.dicimages.get(k)
                    # self.canvas.create_image(((Coord(x,y)-poshero)*64+Coord(401,400)).__index__(),image=image[self.hero.facing.facing()] if n==0 else self.dicanim.get(k)[self.hero.facing.facing()+(4*(n-1))])
                    if type(imagecase) is list:
                        print(f"#{k}#")
                        self.canvas.create_image(
                            (Coord(401, 400)).ind(),
                            image=imagecase[self.hero.facing.facing()]
                            if n == 2
                            else self.dicanim.get(k)[
                                self.hero.facing.facing() + (4 * (n - 2))
                            ],
                        )
                    else:
                        self.canvas.create_image(
                            ((Coord(x, y) - poshero) * 64 + Coord(401, 400)).ind(),
                            image=imagecase,
                        )
                # else:
                #    self.canvas.create_text(((Coord(x,y)-poshero)*64+Coord(401,400)).ind(),text=str(k),font="Arial 32")
                x += 1
            y += 1
        for i in self.floor._attacks:
            self.canvas.create_image(
                ((self.floor._attacks[i] - poshero)
                 * 64 + Coord(401, 400)).ind(),
                image=self.dicatk.get(i.abbrv)[n],
            )

        # truc pour l'interface
        if theGame().hero.hp >= 1:

            # creation de la barre d'inventaire
            self.canvas.create_image(
                50, 400, image=self.dicimages["inventory"])

            # affiche  le niveau de satiete grace a un cookie
            self.canvas.create_image(
                950, 70, image=self.dicimages[f"faim{(theGame().hero.satiete//25)*25}"]
            )

            # affichage de la boite affichant le niveau d'xp et contenant le hero
            experience = theGame().hero.absp
            percent = int(
                ((experience) / (5 + 5 * theGame().hero.level)) * 100)
            if percent >= 90:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox90"])
            elif percent >= 80:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox80"])
            elif percent >= 70:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox70"])
            elif percent >= 60:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox60"])
            elif percent >= 50:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox50"])
            elif percent >= 40:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox40"])
            elif percent >= 30:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox30"])
            elif percent >= 20:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox20"])
            elif percent >= 10:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox10"])
            else:
                self.canvas.create_image(
                    870, 160, image=self.dicimages["herobox0"])

            # affichage du niveau de vie
            for i in range(theGame().hero.hp):
                self.canvas.create_image(
                    130 + 24 * i - (i // 26) * 26 * 24,
                    50 + 40 * (i // 26),
                    image=self.dicimages["health"],
                )

            # affichage des objets dans l'inventaire
            place = 0
            for e in theGame().hero.inventory:
                picture = self.dicinventory.get(e.abbrv)
                self.canvas.create_image(50, 45 + 78 * (place), image=picture)
                place = place + 1

            # affichage des equipements
            self.canvas.create_image(
                870, 300, image=self.dicinventory["equipBar"])
            badge = False
            foulard = False
            plaid = False
            for i in range(4):
                if theGame().hero.equips[i] != None:
                    picture = self.dicequipement[theGame(
                    ).hero.equips[i].abbrv]
                    self.canvas.create_image(811 + 40 * i, 300, image=picture)
                    if theGame().hero.equips[i].name == "plaid":
                        plaid = True
                    if theGame().hero.equips[i].name == "carte de docteur":
                        badge = True
                    if theGame().hero.equips[i].name == "foulard":
                        foulard = True

            # affichage du hero avec les equipements
            if (plaid and badge) == True:
                self.canvas.create_image(
                    875, 185, image=self.dicappear["hero_badgeplaid"]
                )
            elif (plaid and foulard) == True:
                self.canvas.create_image(
                    875, 185, image=self.dicappear["hero_foulardplaid"]
                )
            elif plaid == True:
                self.canvas.create_image(
                    875, 185, image=self.dicappear["hero_plaid"])
            elif badge == True:
                self.canvas.create_image(
                    875, 185, image=self.dicappear["hero_badge"])
            elif foulard == True:
                self.canvas.create_image(
                    875, 185, image=self.dicappear["hero_foulard"])
            else:
                self.canvas.create_image(
                    875, 185, image=self.dicimages["showcase"])

        # minimap
        y = 500
        for i1, i2 in zip(self.seenmap, self.viewablemap):
            x = 800
            for layers in zip(i1, i2):
                for k in layers:
                    if k != Floor.empty:
                        self.canvas.create_image(
                            x, y, image=self.dicseen.get("dy"))
                x += 4
            y += 4

        y = 500
        for i2 in self.viewablemap:
            x = 800
            for k in i2:
                if k != Floor.empty:
                    self.canvas.create_image(
                        x, y, image=self.dicviewable.get("ye"))
                x += 4
            y += 4

        # affichage des emotions
        self.canvas.create_image(
            950, 125, image=self.dicemotion[f"joy{theGame().hero.joie//10 if theGame().hero.joie>=20 else 1}"])
        self.canvas.create_image(
            950, 165, image=self.dicemotion[f"sad{theGame().hero.tristesse//10 if theGame().hero.tristesse>=20 else 1}"])
        self.canvas.create_image(
            950, 205, image=self.dicemotion[f"angry{theGame().hero.colere//10 if theGame().hero.colere>=20 else 1}"])
        self.canvas.create_image(
            950, 245, image=self.dicemotion[f"peur{theGame().hero.peur//10 if theGame().hero.peur>=20 else 1}"])
        # affichage des dialogue dans la boite de dialogue
        self.canvas.create_image(540, 740, image=self.dicimages["dialogue"])
        if last:
            i = 0
            for [message, color, _] in self.readMessages():
                print(message)
                while len(message) > 69:
                    n = 69
                    while not (message[n] in constants.PONCT + " "):
                        n -= 1
                    self.canvas.create_text(
                        540,
                        720 + 25 * i,
                        text=message[:n],
                        font=("Arial 21"),
                        fill=color,
                    )
                    message = message[n:]
                    i += 1
                self.canvas.create_text(
                    540,
                    720 + 25 * i,   # 720 + 25 * (i+1)
                    text=message,
                    font=("Arial 21"),
                    fill=color,
                )
                i += 1

        # affichage du niveau
        self.canvas.create_text(
            870, 68, text=theGame().hero.level, font="Arial 25 bold", fill="white"
        )
        # affichage de la bourse
        self.canvas.create_text(
            870,
            340,
            text=theGame().hero.bourse,
            font="Arial 18 bold",
            fill="white",
            anchor=tkinter.W,
        )
        self.canvas.create_text(
            870,
            370,
            text=theGame().hero.mp,
            font="Arial 18 bold",
            fill="white",
            anchor=tkinter.W,
        )
        self.canvas.create_image(850, 340, image=self.dicinventory["bourse"])
        self.canvas.create_image(850, 370, image=self.dicimages["magic"])

        self.canvas.pack()
        self.fenetre.update()
        if theGame().hero.hp < 1:
            self.endgame()

    def introduction(self):
        print("story")
        random.seed(36)
        self.floor = Floor(20, self.hero)

    def begingame(self):
        """Inits the Game, creates the Tk window and the Canvas, launches the mainloop by executing initgraph.
        \n Not perfect yet"""
        # self.mouse=Controller()
        self.fenetre = tkinter.Tk()
        self.fenetre.title("DG")
        self.fenetre.attributes("-fullscreen", True)
        self.fenetre.configure(background="pink")
        self.canvas = tkinter.Canvas(self.fenetre, width=1200,
                                     height=800, background="black")
        # time.time.sleep(5)
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            85, 120, text="NEW GAME", font="Arial 16 italic", fill="blue"
        )
        # self.bouton_quitter = Button(self.fenetre, text='Quitter', command=self.fenetre.destroy) #utile pour le fullscreen
        # self.bouton_quitter.place(x=1200,y=800)
        self.canvas.delete("all")
        self.canvas.destroy()
        # bouton_jouer = Button(self.fenetre,text='Jouer',command=self.beginplay)
        # bouton_jouer.place(x=1500,y=800)
        self.canvas = tkinter.Canvas(self.fenetre, width=1200,
                                     height=800, background="black")
        self.canvas.place(x=0, y=0)
        bouton_quitter = tkinter.Button(
            self.fenetre, text="Quitter", command=self.fenetre.destroy
        )
        bouton_quitter.place(x=1200, y=800)
        # self.introduction()
        self.buildFloor()
        self.initgraph()

    def endgame(self) -> None:
        "Ends the game"
        self.canvas.delete("all")
        self.canvas.create_image(500, 400, image=self.dicother["gameover"])

    def seeMap(self):
        "Modifies the value of viewablemap and seenmap to match to the tiles viewable and seen."
        theta = 0
        self.viewablemap = [
            [" " for i in range(self.sizemap + 2)] for k in range(self.sizemap + 2)
        ]
        ch = self.floor[theGame().hero]
        while theta <= 2 * math.pi:
            r = 0
            cv = Coord(0, 0)
            while (
                r <= self.hero.distvision
                and (ch + cv in self.floor)
                and (
                    (
                        self.floor[ch + cv] in Floor.listground
                        or self.floor[ch + cv] in Floor.listgroundwet
                    )
                    or self.floor[theGame().hero] == ch + cv
                    or (
                        isinstance(self.floor[ch + cv], Element)
                        and self.floor[ch + cv].transparent == True
                    )
                )
            ):
                self.seenmap[(cv + ch).ord][(cv +
                                             ch).abs] = self.floor[cv + ch]
                self.viewablemap[(cv + ch).ord][(cv +
                                                 ch).abs] = str(self.floor[cv + ch])
                r += 0.2
                cv = Coord(r, theta, True)
            cv = Coord(r + 0.5, theta, True)
            if r < 6 and ch + cv in self.floor:
                self.seenmap[(cv + ch).ord][(cv +
                                             ch).abs] = self.floor[cv + ch]
                self.viewablemap[(cv + ch).ord][(cv +
                                                 ch).abs] = str(self.floor[cv + ch])
            theta += math.pi / 32


def theGame(game=Game()) -> Game:
    "Returns the Game singleton."
    return game


theGame().begingame()
