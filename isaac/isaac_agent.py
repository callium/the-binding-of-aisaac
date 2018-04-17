# This plays the game using physical inputs

import pyautogui
import random
import time
import window_controls as wc

# The Isaac Agent Class
class IsaacAgent:
    APP_NAME = "The Binding of Isaac Afterbirth+"

    # Initialize the object
    def __init__(self):
        self.isPaused = True

    # Run this when the game is first launched to get to the the home page
    def unpause(self):
        if(wc.get_active_window() == self.APP_NAME and self.isPaused == True):
            self.isPaused = False
            time.sleep(.5);
            pyautogui.press('esc')
        if(wc.get_active_window() != self.APP_NAME):
            self.isPaused = True

    # Execute a deliberate movement
    def move(self, direction):
        if(self.isPaused):
            self.unpause()
        else:     
            if(direction == 0): # No movement
                pass
            if(direction == 1): # Up movement
                pyautogui.press('w')
            if(direction == 2): # Down movement
                pyautogui.press('s')
            if(direction == 3): # Left movement
                pyautogui.press('a')
            if(direction == 4): # Right movement
                pyautogui.press('d')
            

    # Execute deliberate shotting
    def shoot(self, direction):
        if(self.isPaused):
            self.unpause()
        else:
            if(direction == 0): # No Shot
                pass
            if(direction == 1): # Down movement
                pyautogui.press('up')
            if(direction == 2): # Left movement
                pyautogui.press('down')
            if(direction == 3): # Left movement
                pyautogui.press('left')
            if(direction == 4): # Right movement
                pyautogui.press('right')


