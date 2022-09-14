import pygame  # import game engine
import ship  # import ship.py which allows access to the general class ship to be used
import images  # import images.py which loads and transforms images


class Player(ship.Ship):  # creates a player class which inherits the properties of the ship class
    def __init__(self, x, y, health=100):  # initializes the object with the following parameters
        super().__init__(x, y, health)  # calls and initializes ship class with the following parameters
        self.ship_img = images.rocket  # sets ship_img to the variable rocket in images.py
        self.bullets_img = images.bullets  # sets bullets_img to the variable bullets in images.py
        self.mask = pygame.mask.from_surface(self.ship_img)  # creates a mask of the surface ship_img for collision
        self.max_health = health  # sets max health for player
