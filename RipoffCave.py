
import time
import TestSecondFile as testName
import ScreenController as ScreenController
import pygame
pygame.init()

gameWindow = pygame.display.set_mode((1200, 500))
#Main file for Ripoff Cave
#define some variables
delay = 0.1

#Define the basic functions
def setup():
    #do setup here
    testName.printHello();
    print("I'm doing setup!");
    ScreenController.CreateWindow()

def mainLoop():
    toPrint = "Main loop! Wee"
    exit_game = False
    while (exit_game == False):
        print(toPrint)

        toPrint = toPrint +"e"
        
        time.sleep(delay)
        
        #check if someone pressed the X button
        if(ScreenController.HasCloseWindowButtonBeenPressed()):
            exit_game = True
    ScreenController.CloseWindow();
#Run them
setup();
mainLoop();