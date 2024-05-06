import pygame
import os


tileWidthInPixels = 64
tilesWide = 19
tilesTall = 8
ownDirectory = os.path.dirname(os.path.realpath(__file__)) #folder that this code was run in
imageDirectory = os.path.join(ownDirectory,"Images")


backgroundPNG = pygame.image.load(os.path.join(imageDirectory,'Background Canopy.png')) # Variable type pygame image?
badGrassPNG = pygame.image.load(os.path.join(imageDirectory,'FirstGrass.png'))
goodGrassPNG = pygame.image.load(os.path.join(imageDirectory,'Grass.png'))
mossPNG = pygame.image.load(os.path.join(imageDirectory,'Mossy Stone.png'))
obsidanPNG = pygame.image.load(os.path.join(imageDirectory,'Obsidian.png'))
stonePNG = pygame.image.load(os.path.join(imageDirectory,'Stone.png'))

gameWindow = pygame.display.set_mode((1200, 500))    # Another weird pygame variable; this one IS a window.


def CreateWindow():
    pygame.init()
    pygame.display.set_caption("Ripoff Cave")


# Ok, so all the drawing the map and the characters stuff needs to be here.
def updateWindow(): 
     gameWindow.blit(backgroundPNG,(0,0))  # 0,0 is top left corner of the screen.    
     pygame.display.update()

def CloseWindow():
    pygame.display.quit()
    pygame.quit()
    quit()



