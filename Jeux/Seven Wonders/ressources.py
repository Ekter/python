class Ressources():
    LISTNAMESRESSOURCES = ["ore", "stone", "wood",
                           "brick", "glass", "paper", "cloth"]

    def __init__(self, name):
        self.name = name
        self.value = 2
        self.enlever = False

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return type(self) == type(other) and self.name == other.name

# test
if __name__ == "__main__":
    print("test")
    ressources = [Ressources(name) for name in Ressources.LISTNAMESRESSOURCES]
    print(ressources)
    print(ressources[0] == ressources[1])
    print(ressources[0] == ressources[0])