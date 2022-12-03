import pygame  # import game engine
import images  # import images.py which loads and transforms images
import player  # import player.py which is the class player which also inherits its properties from ship.py
import satalite
import random
from gameOver import g_over
from menu import menu

pygame.font.init()  # initialize pygame font which is used for rendering fonts
width, height = 600, 720  # height and width of window
owindow = pygame.display.set_mode((width, height))  # initialize the window for display
pygame.display.set_caption("O.S.D")  # name window
pygame.display.set_icon(images.rocket)


# define main
def main():
    menu()
    start = True  # start the infinite loop in "while start"
    fps = 120  # how many frames should pass in a unit of time
    level = 0  # current level player is on
    lives = 3  # current amount of lives player has
    font = pygame.font.SysFont("calibri", 50, bold=True)  # Create a pygame font from system font resources
    player_vel = 5  # velocity of player ship
    num_line = 4

    player.Player = player.Player(250, 595)  # Position on window to place player starting position

    clock = pygame.time.Clock()  # set clock for clock tick

    obs = []
    obs_cor = []
    obs_vel = 4
    r_x = [20, 200, 500, 400, 300, 700, 800, 900, 1000]
    r_y = [-100, -250, -450, -550, -850, -650, -950, -1050, -1200]

    def refresh():
        owindow.blit(images.bg, (0, 0))  # display bg at coord
        player.Player.draw(owindow)  # Place player ship on screen
        dis_lives = font.render(f"Lives: {lives}", True, (255, 255, 255))  # render the font, turn on anti-alias, color
        dis_level = font.render(f"Level: {level}", True, (255, 255, 255))  # render the font, turn on anti-alias, color
        owindow.blit(dis_lives, (10, 10))  # display lives on window at given coords
        owindow.blit(dis_level, (width - dis_level.get_width() - 10, 10))  # display level on window at given coords
        for obstacles in obs:
            obstacles.draw(owindow)
        pygame.display.update()  # update display window

    while start:
        clock.tick(fps)  # Max amount of frames to pass in 1 second
        if len(obs) == 0:
            level += 1
            obs_vel += 0.25
            if level % 4 == 0:
                num_line = int(num_line * 1.25)
            if obs_vel == 8:
                obs_vel = 8
            for i in range(num_line):
                if i % 2 != 0:
                    obstacle = satalite.Obstacle(random.randrange(50, 290), random.randrange(-700, -50),
                                                 random.choice(['satalite1', "satalite2", "shuttle"]))
                else:
                    obstacle = satalite.Obstacle(random.randrange(310, 550), random.randrange(-700, -50),
                                                 random.choice(['satalite1', "satalite2", "shuttle"]))
                obs.append(obstacle)
                obs_cor.append(obstacle.x)
                if i == 4:
                    random.shuffle(r_x)
                    random.shuffle(r_y)

        for move in obs[:]:
            move.obsMove(obs_vel)
            if satalite.Obstacle.collide(move, player.Player):
                lives -= 1
                obs.remove(move)
            try:
                if move.y + obstacle.get_height() > height:
                    lives -= 0
                    obs.remove(move)
            except:
                print('To The Moon!')
        refresh()  # Calls the refresh function

        for event in pygame.event.get():  # look for event
            if event.type == pygame.QUIT:  # close application window
                start = False  # stops infinite loop

        key = pygame.key.get_pressed()  # check to see if a key has been pressed
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and player.Player.x - player_vel > 0:  # check if key a or left
            # has been pressed & creates play boundaries
            player.Player.x -= player_vel  # allows player to move in the x direction (left)
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and player.Player.x + player_vel \
                + player.Player.get_width() < width:  # check if key d or right
            # has been pressed & creates play boundaries
            player.Player.x += player_vel  # allows player to move in the x direction (right)
        if (key[pygame.K_w] or key[pygame.K_UP]) and player.Player.y - player_vel - 50 > 0:  # check if key w or up
            # has been pressed & creates play boundaries
            player.Player.y -= player_vel  # allows player to move in the y direction (up)
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and player.Player.y + player_vel \
                + player.Player.get_height() < height:  # check if key s or down
            # has been pressed & creates play boundaries
            player.Player.y += player_vel  # # allows player to move in the y direction (down)

        if lives == 0:
            x = g_over()
            if x == 1:
                lives = 3
                level -= 1
                obs.clear()
            elif x == 2:
                lives = 3
                level = 0
                obs_vel = 4
                obs.clear()
            elif x == 3:
                quit(True)


main()  # executes main
