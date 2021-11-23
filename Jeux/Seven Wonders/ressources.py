class Ressources():
    listRessources=["Ore","Stone","Wood"]
    def __init__(self,type:int):
        self.name=self.listRessources[type%len(self.listRessources)]

