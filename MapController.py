#This file is in charge of storing and building maps.
# It contains two classes - MapTile and Map.

class MapTile:
    #This Class represents a single map tile. We will use an array of these to represent each map.
    sprite = "grass"
    isWalkable = True
    coordinates = [0, 0]

    # This returns a string when printed from print().
    def __str__(self):
        tileInfo = self.sprite + " " + str(self.coordinates)
        return tileInfo
    
    # This returns a string when printed from arrays (for some reason).
    def __repr__(self):             
        tileInfo = self.sprite + " " + str(self.coordinates)
        return tileInfo

    # This function accepts an integer or sprite name and returns the corresponding tile.
    def __init__(self, type, x = 0, y = 0):
    
        if type == 0:
            self.sprite = "grass"
            self.isWalkable = True

        if type == 1:
            self.sprite = "stone"
            self.isWalkable = False        

        self.coordinates = [x, y]


class Map:

    name = "Map"
    mapArray = []
    xSize = 0
    ySize = 0

    # This function accepts a 2D list of integers and uses it to build a 2D array of map tiles that size.
    def __init__(self, mapGenArray, name = "Basic Map"):
        
        self.name = name

        self.xSize = len(mapGenArray)
        self.ySize = len(mapGenArray[0])

        self.mapArray = [[0 for i in range(self.ySize)] for j in range(self.xSize)]

        for xIndex, tilerow in enumerate(self.mapArray):
            for yIndex, tile in enumerate(tilerow):
                self.mapArray[xIndex][yIndex] = MapTile(mapGenArray[xIndex][yIndex], xIndex*48, yIndex*48)


    # This function returns a nicely aligned string when printed from print().
    def __str__(self):

        neatString = "\n" + self.name + ", Size: " + str(self.xSize) + " " + str(self.ySize) + "\n"

        for xIndex, tilerow in enumerate(self.mapArray):
            for yIndex, tile in enumerate(tilerow):
                neatString += str(self.mapArray[xIndex][yIndex]) + " "
            neatString+="\n"
        
        return neatString
        






manualMap = [[1, 0, 1, 1, 1, 1, 0, 0], 
             [1, 0, 1, 0, 0, 0, 0, 0], 
             [1, 0, 1, 0, 1, 0, 0, 0], 
             [1, 0, 0, 0, 1, 0, 0, 1], 
             [1, 0, 1, 1, 1, 0, 1, 0], 
             [1, 0, 1, 1, 0, 0, 1, 0], 
             [0, 0, 0, 0, 0, 1, 1, 0], 
             [1, 0, 1, 1, 1, 1, 0, 0]]


# print(manualMap)

# baldMap = Map(manualMap)

# print(baldMap)

# testArray = [0, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1, 0]

# print(Map(testArray))

# testArray = [0, 1], [0, 1], [1, 1], [1, 1], [0, 0], [0, 0]

# print(Map(testArray))

# Let's see... I need an array of this shit, alongside some means of contructing them...
# Eventually we'll have a generator to contruct maps for us, but we need a way of doing them manually too.
# That way of doing it manually needs to be at least semi-readable. 



#exit()