import pygame
import random
import images
import ship

pygame.font.init()
width, height = 720, 720  # height and width of window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("O.S.D")  # name window


# define main
def main():
    start = True
    fps = 60  # frames
    level = 1
    lives = 3
    font = pygame.font.SysFont("calibri", 50, bold=True)

    ship_vel = 15

    rocket_ship = ship.Ship(300, 650)

    clock = pygame.time.Clock()  # set clock for clock tick

    def refresh():
        win.blit(images.bg, (0, 0))  # display bg at coord
        dis_lives = font.render(f"Lives: {lives}", True, (255, 255, 255))
        dis_level = font.render(f"Level: {level}", True, (255, 255, 255))
        win.blit(dis_lives, (10, 10))
        win.blit(dis_level, (width - dis_level.get_width() - 10, 10))
        rocket_ship.draw(win)
        pygame.display.update()  # update display window

    while start:
        clock.tick(fps)  # FPS
        refresh()

        for event in pygame.event.get():  # look for event
            if event.type == pygame.QUIT:  # close application window
                start = False

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and rocket_ship.x - ship_vel > 0:
            rocket_ship.x -= ship_vel
        if key[pygame.K_RIGHT] and rocket_ship.x + ship_vel + 50 < width:
            rocket_ship.x += ship_vel
        if key[pygame.K_UP] and rocket_ship.y - ship_vel > 0:
            rocket_ship.y -= ship_vel
        if key[pygame.K_DOWN] and rocket_ship.y + ship_vel + 50 < height:
            rocket_ship.y += ship_vel


main()
