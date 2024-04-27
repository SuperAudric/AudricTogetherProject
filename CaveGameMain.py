# Main file for Ripoff Cave

import time
import ScreenController as ScreenController

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

### THIS IS MAIN DOING MAIN THINGS ###
print("Starting main loop! The game is now running! Yay!")
while (exitGame == False):

    loopCount = loopCount + 1

    # This is screaming "wheee" for some reason.
    scream()

    

    
    ScreenController.updateWindow()
    # Check if someone pressed the X button.
    if(ScreenController.HasCloseWindowButtonBeenPressed()):
        print("Exit button pressed.")
        exitGame = True

    time.sleep(delay)

print("Now exiting.")
ScreenController.CloseWindow()      



