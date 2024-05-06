# Main file for Cave Cave

import time
import ScreenController as ScreenController
import MapController
import InputHandler

# Define Globals
delay = 0.3         # How often we update the screen.
exitGame = False    # Whether we're still running the game.
loopCount = 0   
playerCoords = [3,3]
myInputHandler = InputHandler.inputHandler()
mainMap = MapController.Map(MapController.getTestMap(), "Main Map")

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

def arrayAdd(arr1, arr2):
    outputArray =[]
    for i in range(min(len(arr1),len(arr2))):
        outputArray.append(arr1[i]+arr2[i])
    return outputArray

def handleMovement():
    global playerCoords
    playerMovementDirection = myInputHandler.getPlayerMovement()
    playerCoords = arrayAdd(playerCoords,playerMovementDirection)


# Run setup! Except for all the setup we just did.
setup()

### THIS IS MAIN DOING MAIN THINGS ###
print("Starting main loop! The game is now running! Yay!")
while (exitGame == False):
    loopCount = loopCount + 1
    myInputHandler.getmostRecentFrameEvents(loopCount)
    # This is screaming "wheee" for some reason.
    #scream()
    
    handleMovement()
    

    
    ScreenController.updateWindow(mainMap)
    # Check if someone pressed the X button.
    if(myInputHandler.HasCloseWindowButtonBeenPressed()):
        print("Exit button pressed.")
        exitGame = True

    time.sleep(delay)

print("Now exiting.")
ScreenController.CloseWindow()      



