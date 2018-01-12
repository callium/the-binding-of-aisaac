import os
from AppKit import NSWorkspace

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
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']