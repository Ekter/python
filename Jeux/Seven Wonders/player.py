class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
        self.victory_points = 0
        self.victory_points_per_resource = {
            "wood": 1,
            "stone": 1,
            "brick": 1,
            "wheat": 1,
            "sheep": 1,
            "ore": 1
        }