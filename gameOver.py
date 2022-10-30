import pygame
import images

# initializing and setting text fonts
pygame.font.init()
font = pygame.font.SysFont("calibri", 100, bold=True, italic=True)
font2 = pygame.font.SysFont("calibri", 55, bold=True)
font3 = pygame.font.SysFont("calibri", 45, bold=True)
w = pygame.display.set_mode((600, 720))
# setting text variables
g, c = font.render("Game Over", True, (255, 255, 255)), font2.render("Continue", True, (255, 255, 255))
ng, ex = font2.render("New Game", True, (255, 255, 255)), font2.render("Exit", True, (255, 255, 255))
w.blit(images.bg, (0, 0))


def fade(width, height):        # fades the screen with red
    fade = pygame.Surface((width, height))
    fade.fill((255, 0, 0))      # sets fade color to red
    for alpha in range(0, 100):     # for loop for alpha (opacity)
        fade.set_alpha(alpha)       # sets alpha
        w.blit(images.bg, (0, 0))       # uses the fade specific refresh
        w.blit(fade, (0, 0))        # sets the fade onto the display
        pygame.display.update()
        pygame.time.delay(3)        # delays fade by 3 ms
        pygame.display.update()


def opac():     # sets the opacity from the end of the fade as a background variable in the refreshes
    o = pygame.Surface((600, 720))
    o.fill((255, 0, 0))     # sets color to red
    o.set_alpha(100)        # sets opacity to 100 like the fade
    w.blit(o, (0, 0))       # sets the fade onto the display


def mouse():    # tracks the mouse position to update the color of the rectangles behind yes and no
    m = pygame.mouse.get_pos()

    if 195 <= m[0] <= (195 + c.get_width()) and 260 <= m[1] <= 330:       # looks for mouse in this position on display
        pygame.draw.rect(w, (170, 170, 170), [((600 - c.get_width())/2 - 5), 260, 220, 50])
    else:
        pygame.draw.rect(w, (100, 100, 100), [((600 - c.get_width())/2 - 5), 260, 220, 50])

    if 175 <= m[0] <= (175 + ng.get_width()) and 340 <= m[1] <= 410:
        pygame.draw.rect(w, (170, 170, 170), [((600 - ng.get_width())/2 - 5), 340, 260, 50])
    else:
        pygame.draw.rect(w, (100, 100, 100), [((600 - ng.get_width())/2 - 5), 340, 260, 50])

    if 252.5 <= m[0] <= 350.5 and 420 <= m[1] <= 490:
        pygame.draw.rect(w, (170, 170, 170), [((600 - ex.get_width())/2 - 5), 420, 98, 50])
    else:
        pygame.draw.rect(w, (100, 100, 100), [((600 - ex.get_width())/2 - 5), 420, 98, 50])


def refresh():
    w.blit(images.bg, (0, 0))
    opac()
    w.blit(g, ((600 - g.get_width()) / 2, 100))      # <- sets text on display
    mouse()
    w.blit(c, ((600 - c.get_width()) / 2, 260))     # <-
    w.blit(ng, ((600 - ng.get_width()) / 2, 340))   # <-
    w.blit(ex, ((600 - ex.get_width()) / 2, 420))   # <-


def g_over():
    e = True
    fade(600, 720)  # fades display to red
    pygame.time.delay(200)  # delays pygame to allow time for the fade
    while e:
        pygame.time.delay(1)
        refresh()
        m = pygame.mouse.get_pos()
        for event in pygame.event.get():  # for loop to wait for mouse to click yes or no or exiting pygame
            if event.type == pygame.QUIT:
                quit(True)
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks for mouse clicked within set parameters
                if 195 <= m[0] <= (195 + c.get_width()) and 220 <= m[1] <= 270:
                    return 1
                elif 175 <= m[0] <= (175 + ng.get_width()) and 340 <= m[1] <= 410:
                    return 2
                elif 252.5 <= m[0] <= 350.5 and 420 <= m[1] <= 490:
                    return 3
        pygame.display.update()
