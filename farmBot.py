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

def findAndClickWhenFound(usePath):
    # Will keep looking for the input image until it is found, then click it. Won't exit otherwise
    coords = None
    while coords == None:
        coords = pyautogui.locateOnScreen(usePath, confidence = 0.8)
    click(coords[0], coords[1], coords[2], coords[3])
    time.sleep(1)

def tryFindAndClick(usePath):
    # Will try and find the image, then click it. Returns false and terminates if nothing is found
    coords = pyautogui.locateOnScreen(usePath, confidence = 0.8)
    if coords == None:
        return False
    else:
        click(coords[0], coords[1], coords[2], coords[3])
        time.sleep(1)
        return True

def tryFindLeftMostAndClick(usePath):
    # Will try and find the left-most occurence of an image and click that. Runs once, regardless of whether the image is found or not
    leftMost = 100000
    leftMostIndex = None
    coords = list(pyautogui.locateAllOnScreen(usePath, confidence = 0.8))
    if coords != []:
        for index,coord in enumerate(coords):
            if coord[0] < leftMost:
                leftMost = coord[0]
                leftMostIndex = index
        coords = coords[leftMostIndex]
        click(coords[0], coords[1], coords[2], coords[3])
        time.sleep(1)
        return True
    else:
        return False
        

def homeToStory():
    findAndClickWhenFound("assets\homepage_quest_button.png")
    findAndClickWhenFound("assets\quests_story.jpg")

def storyPlay(ticketLimit):
    counter = 0 # Counter for the tickets spent
    endCounter = 0 #Inactivity counter
    while keyboard.is_pressed('q') == False:
        #Run the various searches, and reset the inactivity counter if they work
        
        failsearch = 0 # Variable that gets incremented every time a search doesn't find its target

        if tryFindAndClick("assets\cutscene_not_done.png"):
            endCounter = 0
        else:
            failsearch += 1

        if tryFindAndClick("assets\cutscene_cleared_screen.png"):
            endCounter = 0
        else:
            failsearch += 1
        
        if tryFindLeftMostAndClick("assets\story_quest_normal_not_done.png"):
            endCounter = 0
        else:
            failsearch += 1

        if tryFindLeftMostAndClick("assets\story_quest_big_not_done.jpg"):
            endCounter = 0
        else:
            failsearch += 1
        
        if tryFindAndClick("assets\prep_for_quest.jpg"):
            endCounter = 0
        else:
            failsearch += 1
        
        if tryFindAndClick("assets\cancel_ally.jpg"):
            endCounter = 0
        else:
            failsearch += 1
        
        if tryFindAndClick("assets\start_normal_1_ticket.jpg"):
            endCounter = 0
        else:
            failsearch += 1
        
        if tryFindAndClick("assets\skip.jpg"):
            endCounter = 0
        else:
            failsearch += 1
        
        if tryFindAndClick("assets\story_next_quest.png") == True:
            counter += 1
            endCounter = 0
        else:
            failsearch += 1

        if ticketLimit != 0:
            if counter >= ticketLimit:
                return True

        if failsearch >= 9:
            # If none of the searches return a positive value, increment the inactivity counter
            endCounter += 1
            if endCounter >= 36:
                # If the inactivity counter reaches the set limit, terminate the function
                return False


# homeToStory()
storyPlay(53)