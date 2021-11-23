from card import Card
from player import Player
from random import randint,choice

class Interface():
    def __init__(self, nbjoueurs: int):
        self.cards = []
        self.players = [
            Player(input(f"Name of player {i}")) for i in range(nbjoueurs-1)]
        for i in range(nbjoueurs):
            self.cards.append(Card("Fonderie", None, {"prod_Ore": 1},))
            self.cards.append(Card("Bibliothèque", None, {"points": 5}))
            self.cards.append(Card("Temple", None, {"points": 2}))
            self.cards.append(Card("Forêt", None, {"prod_Wood": 1}))
            self.cards.append(Card("Carrière", None, {"prod_Stone": 1}))
            self.cards.append(Card("Merveille", None, {"points": 7}))
            self.cards.append(Card("Taverne", None, {"gold": 5, "points": 1}))

    def distribuer(self):
        l = self.cards[:]
        cards2 = []
        while len(l) > 0:
            cards2.append(l.pop(randint(0,len(l)-1)))
        while len(cards2 > 0):
            for i in range(len(self.players)):
                self.players[i].hand.append(cards2.pop(randint(0,len(cards2)-1)))
    
    def tourner(self):
        

