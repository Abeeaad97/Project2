import sys
import pygame


def check(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(aisetitngs, screen, ship):
    screen.fill(aisetitngs.bgcolor)
    ship.blitme()


    pygame.display.flip()