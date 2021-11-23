from ressources import Ressources
from gold import Gold

class Card():
    def __init__(self, name: str, img, values: dict, cost: dict[Ressources|Gold:int]):
        self.__dict__ = {**self.__dict__, **values}
        self.name = name
        self.img = img
