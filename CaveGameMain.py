# Main file for Ripoff Cave

import time
import TestSecondFile as testName
import ScreenController as ScreenController
import pygame

# Define Globals
delay = 0.1         # How often we update the screen.
exitGame = False    # Whether we're still running the game.
loopCount = 0   

# Define Functions
def setup():
    print("Ok, time to start up.")
    print("Let's initialize the window.")
    ScreenController.CreateWindow()

def scream():
    screamString = "Main loop! Whee"
    for x in range(loopCount):
        screamString = screamString + "e"
    print(screamString)




# Run setup! Except for all the setup we just did.
setup()

print("Starting main loop! The game is now running! Yay!")
while (exitGame == False):

    loopCount = loopCount + 1

    # This is screaming "wheee" for some reason.
    scream()

    
    time.sleep(delay)
    
    #check if someone pressed the X button
    if(ScreenController.HasCloseWindowButtonBeenPressed()):
        exitGame = True
ScreenController.CloseWindow()      
# May want to take the main loop out of a function, but put everything it's doing into functions instead so that it's very clearly chunked off with what does what.






