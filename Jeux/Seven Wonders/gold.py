from ressources import Ressources


class Gold(Ressources):
    def __init__(self):
        super(Gold, self).__init__("gold")
        self.value = 1
        self.enlever = True

    # def __str__(self):
    #     return "¤(une pièce)"
