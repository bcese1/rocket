import pygame
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


def menu():
    pygame.mixer.music.load('Interstellar Main Theme - Hans Zimmer.wav')
    pygame.mixer.music.play(-1)
    menuStatus = True
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
                    quit(True)
                # if the mouse is clicked on the button the play-state is launched
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 - 45 <= mouse[1] <= \
                        screenHeight / 2 + 40:
                    # main()

                    # print("start has been pressed")
                    menuStatus = False
                # if the mouse is clicked on the credits screen is launched
                if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 45 <= mouse[1] <= \
                        screenHeight / 2 + 85:
                    print("Credits has been pressed")

        # fills the screen with a color
        screen.fill((60, 25, 60))

        # changes shade to light for exit
        if screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 <= mouse[1] <= \
                screenHeight / 2 + 40:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])

        # changes shade to light for start
        elif screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 - 45 <= mouse[1] <= \
                screenHeight / 2 + 40:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])

        # changes shade to light for credits
        elif screenWidth / 2 - 75 <= mouse[0] <= screenWidth / 2 + 65 and screenHeight / 2 + 45 <= mouse[1] <= \
                screenHeight / 2 + 85:
            pygame.draw.rect(screen, color_light, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 - 45, 140, 40])
            pygame.draw.rect(screen, color_dark, [screenWidth / 2 - 75, screenHeight / 2 + 45, 140, 40])

        # superimposing the text onto our button
        screen.blit(textExit, (screenWidth / 2 - 55, screenHeight / 2))
        screen.blit(textStart, (screenWidth / 2 - 55, screenHeight / 2 - 45))
        screen.blit(textCredits, (screenWidth / 2 - 55, screenHeight / 2 + 45))

        # updates the frames of the game
        pygame.display.update()


