import pygame
import images
import player

pygame.font.init()
width, height = 600, 720  # height and width of window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("O.S.D")  # name window


# define main
def main():
    start = True
    fps = 120  # frames
    level = 1
    lives = 3
    font = pygame.font.SysFont("calibri", 50, bold=True)

    ship_vel = 10

    player.Player = player.Player(250, 595)

    clock = pygame.time.Clock()  # set clock for clock tick

    def refresh():
        win.blit(images.bg, (0, 0))  # display bg at coord
        player.Player.draw(win)
        dis_lives = font.render(f"Lives: {lives}", True, (255, 255, 255))
        dis_level = font.render(f"Level: {level}", True, (255, 255, 255))
        win.blit(dis_lives, (10, 10))
        win.blit(dis_level, (width - dis_level.get_width() - 10, 10))
        pygame.display.update()  # update display window

    while start:
        clock.tick(fps)  # FPS
        refresh()

        for event in pygame.event.get():  # look for event
            if event.type == pygame.QUIT:  # close application window
                start = False

        key = pygame.key.get_pressed()
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and player.Player.x - ship_vel > 0:
            player.Player.x -= ship_vel
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and player.Player.x + ship_vel + player.Player.get_width() < width:
            player.Player.x += ship_vel
        if (key[pygame.K_w] or key[pygame.K_UP]) and player.Player.y - ship_vel - 50 > 0:
            player.Player.y -= ship_vel
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and player.Player.y + ship_vel + player.Player.get_height() < height:
            player.Player.y += ship_vel


main()
