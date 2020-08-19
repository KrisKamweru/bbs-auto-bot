import pyautogui
import time
import keyboard

while keyboard.is_pressed('q') == False:
    pyautogui.displayMousePosition()
    