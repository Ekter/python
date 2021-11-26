from ressources import Ressources

class Raffinated_ressources(Ressources):
    def __init__(self,name):
        super().__init__(name)
        self.value=3

    def __str__(self):
        return self.name
