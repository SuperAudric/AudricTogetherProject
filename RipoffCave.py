# Main file for Ripoff Cave

import time
import TestSecondFile as testName
import ScreenController as ScreenController
import pygame

# Define some variables
delay = 0.1

# Define the basic functions
def setup():
    testName.printHello();        # This is the tiny test file he built first.
    print("I'm doing setup!")
    ScreenController.CreateWindow()            # Wait oh we're initalizing the screen too.

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
    ScreenController.CloseWindow()
    
#Run them
setup()
mainLoop()            
# May want to take the main loop out of a function, but put everything it's doing into functions instead so that it's very clearly chunked off with what does what.






