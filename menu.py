import pygame
import images
# initializing the constructor
pygame.init()

screenWidth, screenHeight = 600, 720

# opens up a window
screen = pygame.display.set_mode((screenWidth, screenHeight))

# white color
white = (255, 255, 255)

# light and shade of the button
color_light, color_dark = (170, 170, 170), (100, 100, 100)

# defining a font
smallFont = pygame.font.SysFont('calibri', 50)
# rendering a text written in
# this font
textExit, textStart = smallFont.render('Exit', True, white), smallFont.render('Start', True, white)
textOption, textCredits = smallFont.render('Options', True, white), smallFont.render('Credits', True, white)
textHTPlay, textPrevious = smallFont.render('How To Play', True, white), smallFont.render('Back', True, white)
textContinue = smallFont.render('Cont.', True, white)
textpaused = pygame.font.SysFont('calibri', 100, bold=True, italic=True).render('Paused', True, white)

def b_left(x): return ((screenWidth - x.get_width()) / 2) - 5


def b_right(x): return (b_left(x) + x.get_width()) + 10


def b_length(x): return x.get_width() + 11


def reverse_fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))  # sets fade color to red
    for alpha in reversed(range(0, 250)):  # for loop for alpha (opacity)
        fade.set_alpha(alpha)  # sets alpha
        screen.blit(images.tsbg, (0, 0))  # uses the fade specific refresh
        screen.blit(fade, (0, 0))  # sets the fade onto the display
        pygame.display.update()
        pygame.time.delay(3)  # delays fade by 3 ms


def mouse_movement():
    # changes shade to light for htp
    mouse = pygame.mouse.get_pos()
    if b_left(textHTPlay) <= mouse[0] <= b_right(textHTPlay) and \
            screenHeight / 2 - 5 <= mouse[1] <= screenHeight / 2 + 42:
        pygame.draw.rect(screen, color_light, [b_left(textHTPlay), screenHeight / 2 - 5, b_length(textHTPlay), 47])
    else:
        pygame.draw.rect(screen, color_dark, [b_left(textHTPlay), screenHeight / 2 - 5, b_length(textHTPlay), 47])
    # changes shade to light for start
    if b_left(textStart) <= mouse[0] <= b_right(textStart) and \
            screenHeight / 2 - 60 <= mouse[1] <= screenHeight / 2 - 20:
        pygame.draw.rect(screen, color_light, [b_left(textStart), screenHeight / 2 - 60, b_length(textStart), 40])
    else:
        pygame.draw.rect(screen, color_dark, [b_left(textStart), screenHeight / 2 - 60, b_length(textStart), 40])
    # changes shade to light for credits
    if b_left(textCredits) <= mouse[0] <= b_right(textCredits) and \
            screenHeight / 2 + 55 <= mouse[1] <= screenHeight / 2 + 95:
        pygame.draw.rect(screen, color_light, [b_left(textCredits), screenHeight / 2 + 55, b_length(textCredits), 40])
    else:
        pygame.draw.rect(screen, color_dark, [b_left(textCredits), screenHeight / 2 + 55, b_length(textCredits), 40])
    # changes shade to light for exit
    if b_left(textExit) + 175 <= mouse[0] <= b_right(textExit) + 175 and \
            screenHeight - 70 <= mouse[1] <= screenHeight - 30:
        pygame.draw.rect(screen, color_light, [b_left(textExit) + 175, screenHeight - 70, b_length(textExit), 40])
    else:
        pygame.draw.rect(screen, color_dark, [b_left(textExit) + 175, screenHeight - 70, b_length(textExit), 40])


def creds_or_htp(value):
    if value == 1:
        c_or_h = images.htp
    elif value == 2:
        c_or_h = images.cred
    while True:
        cmouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if b_left(textPrevious) <= cmouse[0] <= b_right(textPrevious) and \
                        540 <= cmouse[1] <= 580:
                    return False
        screen.blit(c_or_h, (0, 0))
        if b_left(textPrevious) <= cmouse[0] <= b_right(textPrevious) and \
                540 <= cmouse[1] <= 580:
            pygame.draw.rect(screen, color_light,
                             [b_left(textPrevious), 540, b_length(textPrevious), 40])
        else:
            pygame.draw.rect(screen, color_dark, [b_left(textPrevious), 540, b_length(textPrevious), 40])

        screen.blit(textPrevious, (b_left(textPrevious) + 5, 538))

        pygame.display.update()


def pause():
    while True:
        # stores the (x,y) coordinates into the variable as a tuple
        m = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                quit()
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if b_left(textHTPlay) <= m[0] <= b_right(textHTPlay) and screenHeight / 2 - 5 <= m[1] <= \
                        screenHeight / 2 + 42:
                    creds_or_htp(1)
                # if the mouse is clicked on the button the play-state is continued
                if b_left(textContinue) <= m[0] <= b_right(textContinue) and screenHeight / 2 - 60 <= m[1] <= \
                        screenHeight / 2 - 20:
                    return False
                # if the mouse is clicked on the credits screen is launched
                if b_left(textCredits) <= m[0] <= b_right(textCredits) and screenHeight / 2 + 55 <= m[1] <= \
                        screenHeight / 2 + 87:
                    creds_or_htp(2)
                if b_left(textExit) + 175 <= m[0] <= b_right(textExit) + 175 and \
                        screenHeight - 70 <= m[1] <= screenHeight - 30:
                    quit()

        # fills the screen with a color
        opac()
        mouse_movement()
        # superimposing the text onto our button
        screen.blit(textpaused, (b_left(textpaused) + 5, screenHeight / 2 - 262))
        screen.blit(textHTPlay, (b_left(textHTPlay) + 5, screenHeight / 2 - 6))
        screen.blit(textContinue, (b_left(textContinue) + 5, screenHeight / 2 - 62))
        screen.blit(textCredits, (b_left(textCredits) + 5, screenHeight / 2 + 53))
        screen.blit(textExit, (b_left(textExit) + 180, screenHeight - 72))

        # updates the frames of the game
        pygame.display.update()

def opac():  # sets the opacity from the end of the fade as a background variable in the refreshes
    o = pygame.Surface((600, 720))
    o.set_alpha(100)  # sets opacity to 100 like the fade
    screen.blit(o, (0, 0))  # sets the fade onto the display


def menu():
    pygame.mixer.music.load('Interstellar Main Theme - Hans Zimmer.wav')
    pygame.mixer.music.play(-1)
    reverse_fade(screenWidth, screenHeight)
    while True:
        # stores the (x,y) coordinates into the variable as a tuple
        m = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                quit()
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if b_left(textHTPlay) <= m[0] <= b_right(textHTPlay) and screenHeight / 2 - 5 <= m[1] <= \
                        screenHeight / 2 + 42:
                    creds_or_htp(1)
                # if the mouse is clicked on the button the play-state is launched
                if b_left(textStart) <= m[0] <= b_right(textStart) and screenHeight / 2 - 60 <= m[1] <= \
                        screenHeight / 2 - 20:
                    return False
                # if the mouse is clicked on the credits screen is launched
                if b_left(textCredits) <= m[0] <= b_right(textCredits) and screenHeight / 2 + 55 <= m[1] <= \
                        screenHeight / 2 + 87:
                    creds_or_htp(2)
                if b_left(textExit) + 175 <= m[0] <= b_right(textExit) + 175 and \
                        screenHeight - 70 <= m[1] <= screenHeight - 30:
                    quit()


        # fills the screen with a color
        screen.blit(images.tsbg, (0, 0))
        mouse_movement()
        # superimposing the text onto our button
        screen.blit(textHTPlay, (b_left(textHTPlay) + 5, screenHeight / 2 - 6))
        screen.blit(textStart, (b_left(textStart) + 5, screenHeight / 2 - 62))
        screen.blit(textCredits, (b_left(textCredits) + 5, screenHeight / 2 + 53))
        screen.blit(textExit, (b_left(textExit) + 180, screenHeight - 72))

        # updates the frames of the game
        pygame.display.update()
