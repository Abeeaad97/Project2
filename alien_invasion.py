import pygame

import sys

from settings import Settings
from ship import Ship
import game_functions as gf


def play():
    pygame.init()
    aisettings = Settings()
    windowScreen = pygame.display.set_mode(
        (aisettings.screen_width, aisettings.screen_height))

    pygame.display.set_caption('Alien Invasion')
    ship = Ship(windowScreen)

    # Set the background color
    bgcolor = (230, 230, 230)

    game_over = False
    while not game_over:
        gf.check(ship)
        ship.update()
        gf.update_screen(aisettings, windowScreen, ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # redraw the screen during each pass through the loop
            windowScreen.fill(aisettings.bgcolor)
            ship.blitme()

        pygame.display.flip()

play()

