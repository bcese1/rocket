import ship


class Obstacle(ship.Ship):
    obstacle_map = {
                    "satalite1": ()


                    }

    def __init__(self, x, y, color, health=100):
        "satalite1", "satalite2", "shuttle"
        super().__init__(x, y, health)
