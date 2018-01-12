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
        time.sleep(.10)

# Generate a random direction and press the key for that direction
def random_movement(move_time):
    if(wc.get_active_window() == APP_NAME):
        dir = random.randint(0, 3)
        if(dir == 0):
            pyautogui.keyDown('w')
            time.sleep(move_time)
            pyautogui.keyUp('w')
        if(dir == 1):
            pyautogui.keyDown('s')
            time.sleep(move_time)
            pyautogui.keyUp('s')
        if(dir == 2):
            pyautogui.keyDown('a')
            time.sleep(move_time)
            pyautogui.keyUp('a')
        if(dir == 3):
            pyautogui.keyDown('d')
            time.sleep(move_time)
            pyautogui.keyUp('d')

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


def main():
    wc.make_active_window()
    time.sleep(1)
    unpause()
    while(True):
        if(wc.get_active_window() == APP_NAME):
            random_shot()
            move_time = random.randint(1, 100) / 100
            random_movement(move_time)


if __name__ == "__main__":
    main()
