import pygame

gameWindow = pygame.display.set_mode((1200, 500))
def CreateWindow():
    pygame.init()
    pygame.display.set_caption("Ripoff Cave")

    exit_game = False


def CloseWindow():
    pygame.display.quit()
    pygame.quit()
    quit()