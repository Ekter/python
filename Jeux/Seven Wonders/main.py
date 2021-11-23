from card import Card
from player import Player
from ressources import Ressources
from gold import Gold
from random import randint, choice


class Interface():
    def __init__(self, nbjoueurs: int) -> None:
        self.cards = []
        self.players = [
            Player(input(f"Name of player {i}: ")) for i in range(1,nbjoueurs+1)]
        for i in range(nbjoueurs):
            self.cards.append(Card("Fonderie", None, {Gold(): 1}, prod_Ore=1))
            self.cards.append(
                Card("Bibliothèque", None, {Gold(): 1}, points=5))
            self.cards.append(Card("Temple", None,{Gold(): 1}, points=2))
            self.cards.append(Card("Forêt", None, {Gold(): 1},prod_Wood=1))
            self.cards.append(Card("Carrière", None, {Gold(): 1},prod_Stone=1))
            self.cards.append(Card("Merveille", None, {Gold(): 1},points=7))
            self.cards.append(Card("Taverne", None, {Gold(): 1},gold=5, points=1))

    def distribute(self) -> None:
        l = self.cards[:]
        cards2 = []
        while len(l) > 0:
            cards2.append(l.pop(randint(0, len(l)-1)))
        while len(cards2) > 0:
            for i in range(len(self.players)):
                self.players[i].hand.append(
                    cards2.pop(randint(0, len(cards2)-1)))

    def turn_hands(self) -> None:
        handcard=self.players[0].hand
        for i in range(len(self.players)-1):
            self.players[i].hand=self.players[i+1].hand
        self.players[-1].hand=handcard
    
    def play(self) -> None:
        self.distribute()
        self.turn_hands()
        for i in range(7):
            for i in range(len(self.players)):
                print(f"{self.players[i].name}'s turn")
                self.players[i].play()
            self.turn_hands()


if __name__ == "__main__":
    nbjoueurs = int(input("Number of players: "))
    game = Interface(nbjoueurs)
    game.play()