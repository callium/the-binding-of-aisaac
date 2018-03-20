# The Binding of Aisaac

An experiment implementing machine learning to play The Binding of Isaac Afterbirth+

## Basic Information

I believe the best way to procede is to collect points of data (which I have taken to calling beats), then feed those beats into an algorithm that extrapolates certain data (called notes) such as if the agent is in physical contact with any enemies.

The beats will be collected every X seconds. I have yet to determine what time frame will lead to a more efficient program.

All of the genetic information is found in "genetics.py". Sorry if the names are confusing...

As of right now, the beats I plan to collect are: 
    
    movement_direction # Which direction the player is moving which can be used to determine if the player is moving towards or away from an enemy
    
    shot_direction # Same principle as movement direction, but with the damage dealing component of the agent

    player_location # The X & Y coordinate location of the player

    enemy_locations # The X & Y coordinates of all enemies in the room

The points of data extrapolated for the beats are being referred to as notes. These notes are what the fitness algorithm will use to determine how well the agent did (these will reward fitness points):

    enemy_shot_at # Boolean, was the enemy shot at?

    agent_not_in_contact_with_enemy # Boolean, was the agent avoiding an enemy?


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
