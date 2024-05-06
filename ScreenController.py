import pygame
import os
import MapController
from Player import Player
from MapEntity import MapEntity


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
greaterBeanPNG = pygame.image.load(os.path.join(imageDirectory,'TheGreaterBean (ArrowIncluded).png'))
playerPNG = pygame.image.load(os.path.join(imageDirectory,'Player.png'))

gameWindow = pygame.display.set_mode((1200, 500))    # Another weird pygame variable; this one IS a window.


def CreateWindow():
    pygame.init()
    pygame.display.set_caption("Ripoff Cave")


# Ok, so all the drawing the map and the characters stuff needs to be here.
def updateWindow(gameMap:MapController.Map, player:Player): 
    gameWindow.blit(backgroundPNG,(0,0))  # 0,0 is top left corner of the screen.
    for tileRow in gameMap.mapArray:
        for tile in tileRow:
            displayTile(tile)
    displayMapEntity(player,player.coordinates)
    pygame.display.update()

def displayTile(tile:MapController.MapTile):
    image = getPNGFromName(tile.sprite)
    gameWindow.blit(image,(tile.coordinates[0],tile.coordinates[1]))
    if(tile.tileContents != None):
         displayMapEntity(tile.tileContents,tile.coordinates)

def displayMapEntity(mapEntity:MapEntity,coordinates):
    contentsImage = getPNGFromName(mapEntity.sprite)
    gameWindow.blit(contentsImage,(coordinates[0],coordinates[1]))
     

def getPNGFromName(imageName):
    if (imageName == "stone"):
            return stonePNG
    if (imageName == "grass"):
            return goodGrassPNG
    if (imageName == "Greater Bean"):
            return greaterBeanPNG
    if (imageName == "Player"):
            return playerPNG
    else:
        return obsidanPNG

def CloseWindow():
    pygame.display.quit()
    pygame.quit()
    quit()



