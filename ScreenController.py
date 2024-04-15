import pygame
import os

basepath = os.path.dirname(os.path.realpath(__file__)) #folder that this code was run in
background = pygame.image.load(os.path.join(basepath,'Background.png'))
gameWindow = pygame.display.set_mode((1200, 500))


def CreateWindow():
    pygame.init()
    pygame.display.set_caption("Ripoff Cave")
    updateWindow()


def HasCloseWindowButtonBeenPressed():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return True
    return False;

def updateWindow():
     gameWindow.blit(background,(0,0))
     pygame.display.update()

def CloseWindow():
    pygame.display.quit()
    pygame.quit()
    quit()