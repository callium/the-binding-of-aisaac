import pyautogui
import time
import random
import threading
import window_controls as wc
import genetics

# The Isaac Agent Class
class IsaacAgent:
    APP_NAME = "The Binding of Isaac Afterbirth+"
    isMoving = False
    move_time = None
    end_time = None
    isPaused = True

    # Will be used to create a deliberate agent
    album = None

    # Initialize the object
    def _init_(self, **kwargs):
        # Tracks isaac's movement, used in movement logic
        self.isMoving = False
        if(self.isPaused):
            self.unpause()
        
        self.album = kwargs

    # Run this when the game is first launched to get to the the home page
    def unpause(self):
        if(wc.get_active_window() == self.APP_NAME):
            pyautogui.press('esc')
            self.isPaused = False

    # Handles the movement login for random movement
    def random_movement(self):
        if(self.isMoving == False):
            self.move_time = random.randint(0, 100) / 100
            self.end_time = time.time() + self.move_time
            self.start_movement()
            self.isMoving = True
        else:
            if(time.time() >= self.end_time):
                self.end_movement()
                self.isMoving = False

    # Execute a deliberate movement
    def deliberate_movement(self):
        pass

    # Start a movement
    def start_movement(self):
        move_dir = random.randint(0, 4)
        if(move_dir == 0): # Up movement
            pyautogui.keyDown('w')
        if(move_dir == 1): # Down movement
            pyautogui.keyDown('s')
        if(move_dir == 2): # Left movement
            pyautogui.keyDown('a')
        if(move_dir == 3): # Right movement
            pyautogui.keyDown('d')
        if(move_dir == 4): # No movement
            pass

    # End the movement (after some time t)
    def end_movement(self):
        pyautogui.keyUp('w')
        pyautogui.keyUp('s')
        pyautogui.keyUp('a')
        pyautogui.keyUp('d')

    # Shoot in a random direction
    def random_shot(self):
        dir = random.randint(0, 3)
        if(dir == 0):
            pyautogui.press('up')
        if(dir == 1):
            pyautogui.press('down') 
        if(dir == 2):
            pyautogui.press('left')
        if(dir == 3):
            pyautogui.press('right')

    # Execute deliberate shotting
    def deliberate_shot(self, direction):
        pass

    # Initial Random Sequence
    def random_sequence(self):
        # This loop controls the normal movement/shooting
        while(True):    
            if(wc.get_active_window() == isaac_agent.APP_NAME):
                if(self.isPaused):
                    self.unpause()
                else:
                    self.random_movement()
                    self.random_shot()
            else: # Navigated away from isaac
                self.isPaused = True

    # reads data from an album an controls with it
    def controlled_sequence(self):
        pass
