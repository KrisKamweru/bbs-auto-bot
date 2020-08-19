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
usePath = "assets\story_quest_big_not_done.jpg"

# while keyboard.is_pressed('q') == False:
#     if (pyautogui.locateAllOnScreen(usePath, confidence = 0.8) != None) or (pyautogui.locateAllOnScreen(usePath, confidence = 0.8) != ImageNotFoundException):
#         print(list(pyautogui.locateAllOnScreen(usePath, confidence = 0.8)))
#         time.sleep(1)
#     else:
#         print("Not found")
#         time.sleep(1)

# while keyboard.is_pressed('q') == False:
#     if pyautogui.locateOnScreen(usePath, confidence = 0.8) != None:
#         print(pyautogui.locateOnScreen(usePath, confidence = 0.8))
#         time.sleep(1)
#     else:
#         print("Not found")
#         time.sleep(1)