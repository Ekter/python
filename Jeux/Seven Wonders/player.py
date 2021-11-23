from card import Card


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.played_cards = []
        self.gold = 3

    def playCard(self, n: int):
        if n <= 0 or n > len(self.hand):
            return False
        card = self.hand[n-1]
        for i in card.cost:
            print(i.name, i)
            if i.name in self.__dict__ and self.__dict__[i.name] >= card.cost[i]:
                if i.name == "gold":
                    self.gold -= card.cost[i]
                if card in self.hand:
                    self.add_to_played_cards(card)
                    return True
            else:
                print("Vous n'avez pas assez de ressources pour jouer cette carte")
                return False
    
    def add_to_played_cards(self, card):
        self.played_cards.append(card)
        self.hand.remove(card)
        print(card.__dict__)


    def showHand(self):
        for i in self.hand:
            print(i)

    def showPlayedCards(self):
        for i in self.played_cards:
            print(i)

    def play(self):
        print("Vous avez joué:")
        self.showPlayedCards()
        print("Vous avez dans votre main:")
        self.showHand()
        n = -1
        while not(self.playCard(n)):
            n = int(input("Que voulez-vous jouer?"))
        print("c'est bon")
