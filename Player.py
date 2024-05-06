from MapEntity import MapEntity
import InputHandler

class Player(MapEntity):
    myInputHandler: InputHandler

    def __init__(self,playerInputHandler:InputHandler):
        super().__init__("Player")
        self.myInputHandler = playerInputHandler

    
    def handleMovement(self):
        playerMovementDirection = self.myInputHandler.getPlayerMovement()
        self.coordinates = arrayAdd(self.coordinates,playerMovementDirection)



def arrayAdd(arr1, arr2):
    outputArray =[]
    for i in range(min(len(arr1),len(arr2))):
        outputArray.append(arr1[i]+arr2[i])
    return outputArray

