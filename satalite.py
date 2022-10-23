import pygame.mask
import ship
import images


class Obstacle(ship.Ship):
    obstacle_map = {"satalite1": (images.satalite1),
                    "satalite2": (images.satalite2),
                    "shuttle": (images.shuttle)}

    def __init__(self, x, y, color, health=100):
        "satalite1", "satalite2", "shuttle"
        super().__init__(x, y, health)
        self.ship_img = self.obstacle_map[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def obsMove(self, obs_vel):
        self.y += obs_vel