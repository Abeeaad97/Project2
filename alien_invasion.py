import pygame


def play():
    pygame.init()
    windowScreen = pygame.display.set_mode((1200, 700))

    pygame.display.set_caption('Alien Invasion')

    game_over = False
    while not game_over:
        for event in pygame.event.get():


