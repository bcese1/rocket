import pygame


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullets_img = None
        self.bullets = []
        self.bullet_cd = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))

