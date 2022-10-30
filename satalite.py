import pygame.mask
import ship
import images
import random


class Obstacle(ship.Ship):
    obstacle_map = {"satalite1": images.satalite1,
                    "satalite2": images.satalite2,
                    "shuttle": images.shuttle}

    def __init__(self, x, y, health=100):
        super().__init__(x, y)
        pygame.sprite.Sprite.__init__(self)
        self.obstacle_list = [images.satalite1,
                              images.satalite2,
                              images.shuttle]
        self.ship_img = self.obstacle_list[random.randint(0, 2)]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def obsMove(self, obs_vel):
        self.y += obs_vel

    def collide(self, obj2):
        offset_x = obj2.x - self.x
        offset_y = obj2.y - self.y
        return self.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None

