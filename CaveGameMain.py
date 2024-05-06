# Main file for Cave Cave

import time
import ScreenController as ScreenController
import MapController
import InputHandler
from Player import Player
from Enemy import Enemy
# Define Globals
delay = 0.3         # How often we update the screen.
exitGame = False    # Whether we're still running the game.
loopCount = 0   
myInputHandler = InputHandler.inputHandler()
mainMap = MapController.Map(MapController.getTestMap(), "Main Map")
myPlayer = Player(myInputHandler)
testEnemy = Enemy(12)
mainMap.mapArray[2][2].tileContents=testEnemy

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
    myInputHandler.getmostRecentFrameEvents(loopCount)
    # This is screaming "wheee" for some reason.
    #scream()
    
    myPlayer.handleMovement()
    

    
    ScreenController.updateWindow(mainMap,myPlayer)
    # Check if someone pressed the X button.
    if(myInputHandler.HasCloseWindowButtonBeenPressed()):
        print("Exit button pressed.")
        exitGame = True

    time.sleep(delay)

print("Now exiting.")
ScreenController.CloseWindow()      



