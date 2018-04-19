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
* at the moment, this only works on MacOS due to the 'pyautogui' library
* relies on luasockets which can be installed on a mac using luarocks
* the python dependencies can be found in 'requirements.txt'

Steps:

* Copy the '/aimod' folder into '~/Library/Application Support/Binding of Isaac Afterbirth+ Mods' folder

* In Steam, go to 'The Binding of Isaac Afterbirth +' Properties, Set Launch Options, and add the following:
    
    >--luadebug

* This allows luasocket to work with the game.

* Once you have python 3, lua, and all of the dependencies installed, you should be able to run the main file located in the '/isaac' folder using:

    >python3 main.py

* From there, you must first collect data, then you can either train or run. Training is repetitive since the processes is repeated when you run the game. Running train merely tells you the NN training accuracy of your data set.


## Dependencies
    Python 3

    Lua

    See requirements.txt

## Links
Training Video: https://drive.google.com/file/d/17m-35vxboi-q3G1nC9qojVPJeRrAZuJA/view?usp=sharing

1st NN Progress: https://drive.google.com/file/d/1xasceaFqN3ILtiX7_mJt7moQXTzX7pVY/view?usp=sharing
