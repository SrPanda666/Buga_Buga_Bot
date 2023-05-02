import pyautogui as gui
from time import sleep
while True: 
    x,y = gui.position()

    print(f'x = {x}, y = {y}')

    sleep(1)