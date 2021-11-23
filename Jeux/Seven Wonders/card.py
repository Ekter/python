from ressources import Ressources
from gold import Gold


class Card():
    def __init__(self, name: str, color, cost: dict[Ressources:int], **values: dict,):
        self.__dict__ = {**self.__dict__, **values}
        self.name = name
        self.color = color
        self.cost = cost

    def __str__(self):
        return self.name+"\nCost:"+str(self.cost)+"\n"
