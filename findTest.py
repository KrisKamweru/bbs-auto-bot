# =================================================
# ==================== IMPORTS ====================
# =================================================
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# usePath = ""
def multiLookFor(usePath):
    while keyboard.is_pressed('q') == False:
        coords = list(pyautogui.locateAllOnScreen(usePath, confidence = 0.8))
        if coords != []:
            print(coords)
            time.sleep(1)
        else:
            print("Not found")
            time.sleep(1)

def lookFor(usePath):
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen(usePath, confidence = 0.8) != None:
            print(pyautogui.locateOnScreen(usePath, confidence = 0.7))
            time.sleep(1)
        else:
            print("Not found")
            time.sleep(1)

usePath = "assets\story_quest_normal_not_done.png"

# multiLookFor(usePath)
# lookFor(usePath)