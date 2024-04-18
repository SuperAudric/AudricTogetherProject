import pygame
import os

ownDirectory = os.path.dirname(os.path.realpath(__file__)) #folder that this code was run in
background = pygame.image.load(os.path.join(ownDirectory,'Background.png')) # Variable type pygame image?
gameWindow = pygame.display.set_mode((1200, 500))    # Another weird pygame variable; this one IS a window.


def CreateWindow():
    pygame.init()
    pygame.display.set_caption("Ripoff Cave")
    updateWindow()            # This would normally be called every frame to update, but here is only updating once ever.


def HasCloseWindowButtonBeenPressed():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return True
    return False

# Ok, so all the drawing the map and the characters stuff needs to be here.
def updateWindow(): 
     gameWindow.blit(background,(0,0))  # 0,0 is top left corner of the screen.
     pygame.display.update()

def CloseWindow():
    pygame.display.quit()
    pygame.quit()
    quit()



