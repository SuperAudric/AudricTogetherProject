class MapEntity:
    coordinates =[0,0]
    sprite = "Greater Bean"
    walkable = False
    
    def __init__(self,spriteName):
        if(spriteName != None):
            self.sprite = spriteName
    