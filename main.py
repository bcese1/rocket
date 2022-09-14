import pygame  # import game engine
import images  # import images.py which loads and transforms images
import player  # import player.py which is the class player which also inherits its properties from ship.py

pygame.font.init()  # initialize pygame font which is used for rendering fonts
width, height = 600, 720  # height and width of window
win = pygame.display.set_mode((width, height))  # initialize the window for display
pygame.display.set_caption("O.S.D")  # name window


# define main
def main():
    start = True  # start the infinite loop in "While start"
    fps = 120  # how many frames should pass in a unit of time
    level = 1  # current level player is on
    lives = 3  # current amount of lives player has
    font = pygame.font.SysFont("calibri", 50, bold=True)  # Create a pygame font from system font resources

    player_vel = 10  # velocity of player ship

    player.Player = player.Player(250, 595)  # Position on window to place player starting position

    clock = pygame.time.Clock()  # set clock for clock tick

    def refresh():
        win.blit(images.bg, (0, 0))  # display bg at coord
        player.Player.draw(win)  # Place player ship on screen
        dis_lives = font.render(f"Lives: {lives}", True, (255, 255, 255))  # render the font, turn on anti-alias, color
        dis_level = font.render(f"Level: {level}", True, (255, 255, 255))  # render the font, turn on anti-alias, color
        win.blit(dis_lives, (10, 10))  # display lives on window at given coords
        win.blit(dis_level, (width - dis_level.get_width() - 10, 10))  # display level on window at given coords
        pygame.display.update()  # update display window

    while start:
        clock.tick(fps)  # Max amount of frames to pass in 1 second
        refresh()

        for event in pygame.event.get():  # look for event
            if event.type == pygame.QUIT:  # close application window
                start = False  # stops infinite loop

        key = pygame.key.get_pressed()  # check to see if a key has been pressed
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and player.Player.x - player_vel > 0:
            player.Player.x -= player_vel
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and player.Player.x + player_vel + player.Player.get_width() < width:
            player.Player.x += player_vel
        if (key[pygame.K_w] or key[pygame.K_UP]) and player.Player.y - player_vel - 50 > 0:
            player.Player.y -= player_vel
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and player.Player.y + player_vel + player.Player.get_height() < height:
            player.Player.y += player_vel


main()
