class Ressources():
    # listRessources=["Ore","Stone","Wood"]
    def __init__(self,name):
        self.name=name
        self.value=2

    def __str__(self):
        return self.name