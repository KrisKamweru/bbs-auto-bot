from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(4)

def click(x,y):
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def startUp():
    while 1:
        if pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8) != None:
            print("found")
            sleep(3)
            x,y = pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8)
            click(x,y)
            return True

if pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8) != None:
    while 1:
        l = pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8)
        try:
            x = (pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8))[0]
            print(x)
            print(type(x))
            time.sleep(0.5)
        except TypeError:
            print("Not there")
        print(l)
        print(type(l))
        time.sleep(1)
        

#while keyboard.is_pressed('q') == False:
#    retValue = False
#
#    while retValue == False:
#        retValue = startUp()
#    while 1:
#        print("ay?")
#        time.sleep(1)
# while


    
