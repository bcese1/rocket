import pygame  # import game engine
import images  # import images.py which loads and transforms images
import player  # import player.py which is the class player which also inherits its properties from ship.py
import satalite
import random

pygame.font.init()  # initialize pygame font which is used for rendering fonts
width, height = 600, 720  # height and width of window
owindow = pygame.display.set_mode((width, height))  # initialize the window for display
pygame.display.set_caption("O.S.D")  # name window


# define main
def main(obs_vel=None):
    start = True  # start the infinite loop in "while start"
    fps = 120  # how many frames should pass in a unit of time
    level = 0  # current level player is on
    lives = 3  # current amount of lives player has
    font = pygame.font.SysFont("calibri", 50, bold=True)  # Create a pygame font from system font resources

    player_vel = 5  # velocity of player ship

    player.Player = player.Player(250, 595)  # Position on window to place player starting position

    clock = pygame.time.Clock()  # set clock for clock tick

    obs = []
    num_line = level
    obs_vel = 1

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
            num_line += level
            for i in range(num_line):
                obstacle = satalite.Obstacle(random.randrange(50, width-100), random.randrange(-1500, -100),
                                             random.choice(['satalite1', "satalite2", "shuttle"]))
                obs.append(obstacle)
        for move in obs[:]:
            move.obsMove(obs_vel)
            if move.y + move.get_height() > height:
                lives -= 1
                obs.remove(move)
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


main()  # executes main
