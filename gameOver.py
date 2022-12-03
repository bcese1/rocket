import pygame
import images
import random
from menu import b_left, b_length, b_right

# initializing and setting text fonts
pygame.font.init()
font = pygame.font.SysFont("calibri", 100, bold=True, italic=True)
font2 = pygame.font.SysFont("calibri", 50)
font3 = pygame.font.SysFont("calibri", 23, bold=True)
w = pygame.display.set_mode((600, 720))
# setting text variables
g, c = font.render("Game Over", True, (255, 255, 255)), font2.render("Continue", True, (255, 255, 255))
ng, ex = font2.render("New Game", True, (255, 255, 255)), font2.render("Exit", True, (255, 255, 255))
sf, ba = font2.render("Space Debris Fact", True, (255, 255, 255)), font2.render("Back", True, (255, 255, 255))
nf = font2.render("New Fact", True, (255, 255, 255))
w.blit(images.bg, (0, 0))

s_facts = "space_facts.txt"
s_list = []
try:        # This is using with to read the text file safely into the patient list
    with open(s_facts, 'r') as hand:
        a = hand.read().split("\n\n")
        for x in a:
            s_list.append(x)
except FileNotFoundError:   # If this error occurs it will be caught
    print("File cannot be opened:", s_facts)
    exit()


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

    if b_left(c) <= m[0] <= b_right(c) and 260 <= m[1] <= 305:       # looks for mouse in this position on display
        pygame.draw.rect(w, (170, 170, 170), [b_left(c), 260, b_length(c), 45])
    else:
        pygame.draw.rect(w, (100, 100, 100), [b_left(c), 260, b_length(c), 45])
    if b_left(ng) <= m[0] <= b_right(ng) and 320 <= m[1] <= 365:
        pygame.draw.rect(w, (170, 170, 170), [b_left(ng), 320, b_length(ng), 45])
    else:
        pygame.draw.rect(w, (100, 100, 100), [b_left(ng), 320, b_length(ng), 45])
    if b_left(sf) <= m[0] <= b_right(sf) and 380 <= m[1] <= 425:
        pygame.draw.rect(w, (170, 170, 170), [b_left(sf), 380, b_length(sf), 45])
    else:
        pygame.draw.rect(w, (100, 100, 100), [b_left(sf), 380, b_length(sf), 45])
    if b_left(ex) + 175 <= m[0] <= b_right(ex) + 175 and 650 <= m[1] <= 695:
        pygame.draw.rect(w, (170, 170, 170), [b_left(ex) + 175, 650, b_length(ex), 45])
    else:
        pygame.draw.rect(w, (100, 100, 100), [b_left(ex) + 175, 650, b_length(ex), 45])


def refresh():
    w.blit(images.bg, (0, 0))
    opac()
    w.blit(g, (b_left(g) + 5, 100))      # <- sets text on display
    mouse()
    w.blit(c, (b_left(c) + 5, 260))      # <-
    w.blit(ng, (b_left(ng) + 5, 320))    # <-
    w.blit(sf, (b_left(sf) + 5, 380))    # <-
    w.blit(ex, (b_left(ex) + 180, 650))  # <-


def space_fact():
    temp = s_list[random.randint(0, 15)]
    while True:
        m2 = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if b_left(ba) <= m2[0] <= b_right(ba) and 540 <= m2[1] <= 580:
                    return False
                if b_left(nf) <= m2[0] <= b_right(nf) and 490 <= m2[1] <= 530:
                    temp = s_list[random.randint(0, 15)]

        w.blit(images.bg, (0, 0))
        opac()
        if b_left(ba) <= m2[0] <= b_right(ba) and 540 <= m2[1] <= 580:
            pygame.draw.rect(w, (170, 170, 170), [b_left(ba), 540, b_length(ba), 40])
        else:
            pygame.draw.rect(w, (100, 100, 100), [b_left(ba), 540, b_length(ba), 40])
        if b_left(nf) <= m2[0] <= b_right(nf) and 490 <= m2[1] <= 530:
            pygame.draw.rect(w, (170, 170, 170), [b_left(nf), 490, b_length(nf), 40])
        else:
            pygame.draw.rect(w, (100, 100, 100), [b_left(nf), 490, b_length(nf), 40])

        w.blit(ba, (b_left(ba) + 5, 538))
        w.blit(sf, (b_left(sf) + 5, 50))
        w.blit(nf, (b_left(nf) + 5, 488))
        q = str(temp).split(sep="\n")
        q = [z.strip() for z in q]
        for b in range(0, len(q)):
            temp2 = font3.render(q[b], True, (255, 255, 255))
            if b == 0:
                w.blit(temp2, (b_left(temp2) + 5, 200))
            elif b == 1:
                w.blit(temp2, (b_left(temp2) + 5, 245))
            elif b == 2:
                w.blit(temp2, (b_left(temp2) + 5, 290))
            elif b == 3:
                w.blit(temp2, (b_left(temp2) + 5, 335))
            elif b == 4:
                w.blit(temp2, (b_left(temp2) + 5, 380))
            elif b == 5:
                w.blit(temp2, (b_left(temp2) + 5, 425))

        pygame.display.update()


def g_over():
    fade(600, 720)  # fades display to red
    while True:
        refresh()
        m = pygame.mouse.get_pos()
        for event in pygame.event.get():  # for loop to wait for mouse to click yes or no or exiting pygame
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks for mouse clicked within set parameters
                if b_left(c) <= m[0] <= b_right(c) and 260 <= m[1] <= 305:
                    return 1
                elif b_left(ng) <= m[0] <= b_right(ng) and 320 <= m[1] <= 365:
                    return 2
                elif b_left(sf) <= m[0] <= b_right(sf) and 380 <= m[1] <= 425:
                    space_fact()
                elif b_left(ex) + 175 <= m[0] <= b_right(ex) + 175 and 650 <= m[1] <= 695:
                    return 3

        pygame.display.update()
