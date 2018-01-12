import pyautogui
import time
import random
import threading
import window_controls as wc

APP_NAME = "The Binding of Isaac Afterbirth+"

# Run this when the game is first launched to get to the the home page
def unpause():
    if(wc.get_active_window() == APP_NAME):
        pyautogui.press('space')

# Generate a random direction and press the key for that direction
def random_movement():
    move_time = random.randint(1, 100) / 100
    end_time = time.time() + move_time
    if(wc.get_active_window() == APP_NAME):
        dir = random.randint(0, 4)
        if(dir == 0): # Up movement
            pyautogui.keyDown('w')
            time.sleep(move_time)
            pyautogui.keyUp('w')
        if(dir == 1): # Down movement
            pyautogui.keyDown('s')
            time.sleep(move_time)
            pyautogui.keyUp('s')
        if(dir == 2): # Left movement
            pyautogui.keyDown('a')
            time.sleep(move_time)
            pyautogui.keyUp('a')
        if(dir == 3): # Right movement
            pyautogui.keyDown('d')
            time.sleep(move_time)
            pyautogui.keyUp('d')
        if(dir == 4): # No movement
            time.sleep(move_time)

# Start a random movement
def start_random_movement():
    pass

# End the movement (after some time t)
def end_random_movement(direction):
    pass

# Execute deliberate movement (direction and time to hold the key)
def start_deliberate_movement(direction):
    pass

# End the deliberate shooting
def end_deliberate_movement(direction):
    pass

# Shoot in a random direction
def random_shot():
    if(wc.get_active_window() == APP_NAME):
        dir = random.randint(0, 3)
        if(dir == 0):
            pyautogui.press('up')
        if(dir == 1):
            pyautogui.press('down') 
        if(dir == 2):
            pyautogui.press('left')
        if(dir == 3):
            pyautogui.press('right')

# Begin random shot
def start_random_shot():
    pass

# End random shot
def end_random_shot():
    pass

# Execute deliberate shotting
def start_deliberate_shot(direction):
    pass

# End a deliberate shot
def end_deliberate_shot(direction):
    pass

def main():
    wc.open_isaac()
    wc.make_active_window()
    time.sleep(1)

    # This loop controls the normal movement/shooting
    while(True):
        if(wc.get_active_window() == APP_NAME):
            random_shot()
            random_movement()


if __name__ == "__main__":
    main()
