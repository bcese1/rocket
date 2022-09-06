import pygame
import ship
import images


class Player(ship.Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = images.rocket
        self.bullets_img = images.bullets
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
