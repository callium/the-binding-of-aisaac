# The Binding of Aisaac

An experiment implementing machine learning to play The Binding of Isaac Afterbirth+

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

### At the time of writing this, there is no artificial intelligence involved, just random movement & shot direction
