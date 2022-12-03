import pygame

import images

# initializing the constructor
pygame.init()

screenWidth = 600
screenHeight = 720

# opens up a window
screen = pygame.display.set_mode((screenWidth, screenHeight))

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# defining a font
smallFont = pygame.font.SysFont('calibri', 35)

# rendering a text written in
# this font
textExit = smallFont.render('Exit', True, color)
textStart = smallFont.render('Start', True, color)
textOption = smallFont.render('Options', True, color)
textCredits = smallFont.render('Credits', True, color)
textHTPlay = smallFont.render('How To', True, color)
textPrevious = smallFont.render('Back', True, color)
htpflag = 0


def menu():
    global htpflag
    # pygame.mixer.music.load('Interstellar Main Theme - Hans Zimmer.wav')
    # pygame.mixer.music.play(-1)
    menuStatus = True
    reverse_fade(screenWidth, screenHeight)
    # pygame.time.delay(280)
    while menuStatus:
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                quit(True)

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 <= mouse[1] <= \
                        screenHeight / 2 + 40:
                    howToPay()
                # if the mouse is clicked on the button the play-state is launched
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 - 45 <= mouse[1] <= \
                        screenHeight / 2 + 40:
                    menuStatus = False
                # if the mouse is clicked on the credits screen is launched
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 45 <= mouse[1] <= \
                        screenHeight / 2 + 85:
                    credits()
                # if the mouse is clicked on the how to play is pulled up
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 90 <= mouse[1] <= \
                        screenHeight / 2 + 130:
                    quit(True)

        # sets the title screen background
        screen.blit(images.tsbg, (0, 0))

        # changes shade to light for exit
        if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 <= mouse[1] <= \
                screenHeight / 2 + 40:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 90, 140, 40])

        # changes shade to light for start
        elif screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 - 45 <= mouse[1] <= \
                screenHeight / 2 + 40:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 90, 140, 40])

        # changes shade to light for credits
        elif screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 45 <= mouse[1] <= \
                screenHeight / 2 + 85:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 90, 140, 40])

        # changes shade to light for how to play
        elif screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 90 <= mouse[1] <= \
                screenHeight / 2 + 130:
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 + 90, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 90, 140, 40])

        # superimposing the text onto our button
        screen.blit(textExit, (screenWidth / 2 - 55, screenHeight / 2 + 90))
        screen.blit(textStart, (screenWidth / 2 - 55, screenHeight / 2 - 45))
        screen.blit(textCredits, (screenWidth / 2 - 55, screenHeight / 2 + 45))
        screen.blit(textHTPlay, (screenWidth / 2 - 55, screenHeight / 2))

        # updates the frames of the game
        pygame.display.update()

def howToPay():
    global htpflag
    howToStatus = True
    while howToStatus:

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 180 <= mouse[1] <= \
                        screenHeight / 2 + 220:
                    menu()

        screen.blit(images.htp, (0, 0))

        if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 180 <= mouse[1] <= \
                screenHeight / 2 + 220:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 + 180, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 180, 140, 40])

        screen.blit(textPrevious, (screenWidth / 2 - 55, screenHeight / 2 + 180))

        pygame.display.update()


def reverse_fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))  # sets fade color to black
    for alpha in reversed(range(0, 250)):  # for loop for alpha (opacity)
        fade.set_alpha(alpha)  # sets alpha
        screen.blit(images.tsbg, (0, 0))  # sets background
        screen.blit(fade, (0, 0))  # sets the fade onto the display
        pygame.display.update()
        pygame.time.delay(3)  # delays fade by 3 ms

def credits():
    howToStatus = True
    while howToStatus:

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 180 <= mouse[1] <= \
                        screenHeight / 2 + 220:
                    menu()

        screen.blit(images.cred, (0, 0))

        if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 180 <= mouse[1] <= \
                screenHeight / 2 + 220:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 + 180, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 180, 140, 40])

        screen.blit(textPrevious, (screenWidth / 2 - 55, screenHeight / 2 + 180))

        pygame.display.update()