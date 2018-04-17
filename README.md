# The Binding of Aisaac

An experiment implementing machine learning to play The Binding of Isaac Afterbirth+

## Basic Information

Tensorflow will use training data and learn how to produce expected results.

There will be 4 input points of data => [enemy above, enemy below, enemy left, enemy right] and 2 output points => [movement_direction, shot_direction]
    
    Is there an enemy above the player => bool as integer

    Is there an enemy below the player => bool as integer

    Is there an enemy to the right of the player => bool as integer
    
    Is there an enemy to the left of the player => bool as integer

    movement_direction # Which direction the player is moving which can be used to determine if the player is moving towards or away from an enemy => integer
    
    shot_direction # Same principle as movement direction, but with the damage dealing component of the agent => integer

## Instructions
* must own The Binding of Isaac Afterbirth+ (on Steam)
* at the moment, this only works on MacOS due to system commands
* relies on luasockets which can be installed on a mac by
    luarocks install luasocket

Copy the /aimod folder into '~/Library/Application Support/Binding of Isaac Afterbirth+ Mods' folder

In Steam, go to 'The Binding of Isaac Afterbirth +' Properties, Set Launch Options, and add the following:
    --luadebug
For some reason this is needed to allow the luasocket to work

## Dependencies
See requirements.txt

## Links

Training Video: https://drive.google.com/file/d/17m-35vxboi-q3G1nC9qojVPJeRrAZuJA/view?usp=sharing
