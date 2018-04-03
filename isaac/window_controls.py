# Helper controls for the program

import os
from AppKit import NSWorkspace

# This will open the game
def open_isaac():
    command = """
        open steam://run/250900
    """
    os.system(command)

def close_isaac():
    command = """
        osascript - e 'quit app "The Binding of Isaac Rebirth"'
    """
    os.system(command)

# Uses applescript to move the Binding of Isaac window to the foreground
# Later, I will try to create a python module to do this using system codes
# rather than applescript
def make_active_window():
    command = """
        osascript -e 'tell application "The Binding of Isaac Rebirth" to activate'
    """
    os.system(command)


# Get the name of the active window
def get_active_window():
    # print(NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']