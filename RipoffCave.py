
import time


#Main file for Ripoff Cave
#define some variables
delay = 0.1

#Define the basic functions
def setup():
    #do setup here
    print("I'm doing setup!");

def mainLoop():
    toPrint = "Main loop! Wee"
    while (True):
        print(toPrint)

        toPrint = toPrint +"e"
        
        time.sleep(delay)
#Run them
setup();
mainLoop();