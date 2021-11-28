class Ressources():
    # listRessources=["Ore","Stone","Wood"]
    def __init__(self, name):
        self.name = name
        self.value = 2
        self.enlever = False

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return self.name == other.name
