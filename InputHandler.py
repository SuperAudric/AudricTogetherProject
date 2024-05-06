import pygame

class inputHandler:
    
    events = []
    timeOfLastCalculation=-1
    counter = 0

    #this clears the events, which I only want to do once per frame
    def getmostRecentFrameEvents(self, currentGameFrame):
        if self.timeOfLastCalculation <currentGameFrame:
            self.timeOfLastCalculation = currentGameFrame
            self.events = pygame.event.get()

    def HasCloseWindowButtonBeenPressed(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return True
        return False

    def getPlayerMovement(self):
        movementDirection = [0,0]
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     movementDirection[0]-=64;
                if event.key == pygame.K_RIGHT:
                     movementDirection[0]+=64;
                if event.key == pygame.K_DOWN:
                     movementDirection[1]+=64;
                if event.key == pygame.K_UP:
                     movementDirection[1]-=64;
        return movementDirection
