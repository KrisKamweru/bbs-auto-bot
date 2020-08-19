from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(4)

# The following code was used to test the button pushes on a 1920*1080 screen:
# https://codepen.io/gregjha/pen/MWyemyB
# it is from this pen that the button images are sourced

# Function that accepts the x and y values of the top left corner of the found iamges, as well as the width and height of the found images, and uses the width and height to click in the center of the image
def click(x,y, width, height):
    win32api.SetCursorPos((x + int(width/2),y + int(height/2)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x + int(width/2),y + int(height/2), 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x + int(width/2),y + int(height/2), 0, 0)

# Iteration variable for the click test
iteration = 1

# Click the two buttons in alternating fashion
while keyboard.is_pressed('q') == False:    
    if iteration == 1:
        usePath = 'assets/html_button_accept.png'
    else:
        usePath = 'assets/html_button_cancel.png'
    
    find = pyautogui.locateOnScreen(usePath, confidence = 0.8)
    
    if find != None:
        if iteration == 1:
            iteration = 2
        else:
            iteration = 1
        click(find[0], find[1], find[2], find[3])
        time.sleep(1)
        
    else:
        print("Not found!")
        time.sleep(1)

# def startUp():
#     while 1:
#         if pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8) != None:
#             print("found")
#             sleep(3)
#             x,y = pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8)
#             click(x,y)
#             return True

# if pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8) != None:
#     while 1:
#         l = pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8)
#         try:
#             x = (pyautogui.locateOnScreen('assets/homepage_quests.jpg', confidence=0.8))[0]
#             print(x)
#             print(type(x))
#             time.sleep(0.5)
#         except TypeError:
#             print("Not there")
#         print(l)
#         print(type(l))
#         time.sleep(1)
        

#while keyboard.is_pressed('q') == False:
#    retValue = False
#
#    while retValue == False:
#        retValue = startUp()
#    while 1:
#        print("ay?")
#        time.sleep(1)
# while


    
