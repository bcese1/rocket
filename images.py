import pygame  # import game engine

# load space debris
satalite1 = pygame.image.load('Images/satallie1.png')  # loads satallie1.png from the images folder
satalite2 = pygame.image.load('Images/satallie2.png')  # loads satallie2.png from the images folder
shuttle = pygame.image.load('Images/Shuttle.png')  # loads Shuttle.png from the images folder

# load player rocket
rocket = pygame.image.load('Images/rocket.png')  # loads rocket.png from the images folder
rocket = pygame.transform.smoothscale(rocket, (95, 95))  # transforms the image rocket.png to a smaller LxW

# load player ammo
bullets = pygame.image.load('Images/bullets.png')  # loads bullets.png from the images folder

# load background
bg = pygame.image.load('Images/bg.png')  # loads bg.png from the images folder

# Title Screen Background
tsbg = pygame.image.load('Images/thumbnail_TSBackground.png')

cred = pygame.image.load('Images/credits.png')

htp = pygame.image.load('Images/HowToPlay.PNG')