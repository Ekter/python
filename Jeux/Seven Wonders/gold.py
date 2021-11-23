from ressources import Ressources

class Gold(Ressources):
    def __init__(self):
        super().__init__("gold")
        self.value=1

    def __str__(self):
        return "¤(une pièce)"