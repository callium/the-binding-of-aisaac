# The Binding of Aisaac

An experiment implementing machine learning to play The Binding of Isaac Afterbirth+

## Basic Information

I believe the best way to procede is to collect points of data (which I have taken to calling beats), then feed those beats into an algorithm that extrapolates certain data (called notes) such as if the agent is in physical contact with any enemies.

The beats will be collected every X seconds. I have yet to determine what time frame will lead to a more efficient program.

All of the genetic information is found in "genetics.py". Sorry if the names are confusing...

As of right now, the beats I plan to collect are:  
    
    movement_direction # Which direction the player is moving which can be used to determine if the player is moving towards or away from an enemy => integer
    
    shot_direction # Same principle as movement direction, but with the damage dealing component of the agent => integer

    player_location # The X & Y coordinate location of the player
    enemy_locations # The X & Y coordinates of all enemies in the room
        is enemy above => bool
        is enemy to the right => bool
        is enemy to the left => bool
        is enemy below => bool
        is enemy close => bool

Tensorflow will take the six points of data along with training data to hopefully produce results
There will be 6 input points of data (move_dir, shot_dir, enem_abov, enem_belo, enem_left, enem_righ)

## Instructions
* must own The Binding of Isaac Afterbirth+ (on Steam)
* at the moment, this only works on MacOS due to system commands
* relies on luasockets which can be installed on a mac by
    luarocks install luasocket

Copy the /aimod folder into '~/Library/Application Support/Binding of Isaac Afterbirth+ Mods' folder

In Steam, go to 'The Binding of Isaac Afterbirth +' Properties, Set Launch Options, and add the following:
    --luadebug
For some reason this is needed to allow the luasocket to work

Install Python 3.6 and run the isaac_agent.py file

At the moment, the program is a little buggy (may take some fiddling to get the game working)
