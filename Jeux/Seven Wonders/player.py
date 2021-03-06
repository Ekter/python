from ressources import Ressources
from gold import Gold


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.played_cards = []
        for i in Ressources.LISTNAMESRESSOURCES:
            self.__dict__[Ressources(i)] = 0
        self.__dict__[Gold()] = 3

    def playCard(self, n: int):
        if n <= 0 or n > len(self.hand):
            print("Vous n'avez pas de carte à cette position" if n != 37 else "")
            return False
        card = self.hand[n-1]
        for i in card.cost:
            print(i, type(i))
            if not(i in self.__dict__):
                # TODO changer ça
                print(
                    f"Vous n'avez pas assez de ressources pour jouer cette carte,il vous faudrait de la {i.name}")
                return False
            if self.__dict__[i] < card.cost[i]:
                print(
                    f"Vous n'avez pas assez de ressources pour jouer cette carte, il vous faudrait plus de {i.name}")
                return False
            if i.enlever:
                self.__dict__[i] -= card.cost[i]
        self.add_to_played_cards(card)
        return True

    def add_to_played_cards(self, card):
        self.played_cards.append(card)
        self.hand.remove(card)
        for effect, value in card.__dict__.items():
            if not(effect in ["name", "color", "cost"]):
                print(f"{effect},{value}")
                if effect in self.__dict__:
                    self.__dict__[effect]+=value
                else:
                    self.__dict__[effect]=value
                    print(effect,value)

    def showHand(self):
        for i in self.hand:
            print(i)

    def showPlayedCards(self):
        for i in self.played_cards:
            print(i)

    def play(self):
        self.print2()
        n = 37
        while not(self.playCard(n)):
            try:
                n = int(input("Que voulez-vous jouer?"))
            except ValueError:
                pass
        print("c'est bon")

    def print2(self) -> str:
        print("Vous avez joué:")
        self.showPlayedCards()
        print("Vous avez dans votre main:")
        self.showHand()
