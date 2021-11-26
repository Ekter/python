from ressources import Ressources


class Card():
    colordict = {1: "bleu", 2: "vert", 3: "rouge",
                 4: "jaune", 5: "violet", 6: "marron", 7: "gris"}

    def __init__(self, name: str, color: int, cost: dict[Ressources:int], **values: dict,):
        self.name = name
        self.color = color
        self.cost = cost
        self.__dict__ = {**self.__dict__, **values}

    def __str__(self):
        return f"""{self.name}({self.colordict[self.color]})
\tCoût : {", ".join([f"{ressource.name}:{value}" for ressource, value in self.cost.items()])}
\tEffets : {", ".join([f"{effect}:{value}" for effect, value in self.__dict__.items(
) if not(effect in ["name","color","cost"])])}"""
