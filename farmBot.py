# =================================================
# ===================== TODO ======================
# =================================================
# Determine all the scenarios bot should cover
# -> Story farming
# -> Crystal/Jewel/Ring farming
# -> Scroll quests
# -> Single player IZ farming 
# -> Coop farming (for Inheritance Zone, Accessory Fusion Trials, Extreme Co-op and Epic Raids):
# - => With Guild Invite
# - => With Public Invite
# - => With first guild invite, then public invite after a delay 
#  
# Determine what images are needed for all scenarios
#  
# Create function for getting from the game load screen to home screen
# Create a function for getting from any screen to the home screen
#
# DONE:: Create click funtion
# Create click and drag function for Epic Raids
#  
# Create function for getting from home screen to:
# -> Story mode main
# - => Normal
# - => Hard 
# 
# -> Story mode side
# - => Normal
# - => Hard
# 
# -> Sub Stories
#  
# -> Single player farming:
# - => Crystals
# - => Jewels
# - => Resurrection Rings
# - => Scrolls
# - => Inheritance Zone
# 
# -> Coop Farming:
# - => Extreme Coop
# - => Inheritance Zone
# - => Extreme Coop
# - => Accessory Fusion Trials 
# 
# Create Next quest function for story mode with ticket limit
# Create retry function for:
# -> Solo farming
# -> Coop IZ, Ex Coop & Powder Farming
# -> ER  

# Function that accepts the x and y values of the top left corner of the found images, 
# as well as the width and height of the found images, 
# and uses the width and height to click in the center of the image

# =================================================
# ==================== IMPORTS ====================
# =================================================
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# =================================================
# =================== FUNCTIONS ===================
# =================================================

# pyautogui.locateOnScreen(usePath, confidence = 0.8)
# keyboard.is_pressed('q') == False

def click(x,y, width, height):
    win32api.SetCursorPos((x + int(width/2),y + int(height/2)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x + int(width/2),y + int(height/2), 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x + int(width/2),y + int(height/2), 0, 0)

def findAndClick(pathValue):
    usePath = pathValue
    coords = None
    while coords == None:
        coords = pyautogui.locateOnScreen(usePath, confidence = 0.8)
    click(coords[0], coords[1], coords[2], coords[3])
    time.sleep(1)

def homeToStory():
    findAndClick("assets\homepage_quest_button.png")
    findAndClick("assets\quests_story.jpg")

homeToStory()