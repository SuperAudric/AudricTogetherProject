This is a project to work together to make a game and an AI to play it.

Our main note page is here.
https://docs.google.com/document/d/1Ahsx2MOUriyxkSEOf4WmTfPmR8vMjah-hjf0bDaudO8/edit

Next task:
Display the grid of map tiles.


**ALL TASKS:**
- Game window. [Done!]
- Grid of map tiles arranged manually. [Done!]
- Sprites to represent floor, walls, player, enemy, statgem. [Need temp player and enemy.]
- Player entity that can move with arrow keys or wads and are blocked by walls.
- Enemy entities with stats.
- Combat mechanism when player steps on an enemy.
- Stat gems that increase player stats when walked behind.
- MAP generation. Will take a lot.
- Bots!

**STRUCTURE:**
- Main -
    Runs set up functions, then, launches window, watches for inputs and runs main gameplay loop.
- Screen Handler -
    Draws each frame and moves sprites around as instructed.
- Map Handler -
    Defines, creates and stores map tiles and grids of map tiles. May add the generator to this file too.
- Map Generator? -
    Generates the map at the start of each floor from either a set or randomized seed.
- Entity Handler -
    Defines enemy stats, sprites, states and animation.
- Player -
    Defines player stats, sprites, responses to input, states and animation.

