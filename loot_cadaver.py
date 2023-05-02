import pyautogui as gui

from time import sleep

def lotear_capturar(x,y):
    gui.moveTo(x,y)
    sleep(0.25)
    gui.rightClick()
    gui.moveTo(x=1189, y=514)
    gui.leftClick()
    gui.leftClick()
    gui.leftClick()
    gui.leftClick()
    sleep(0.25)
    #gui.moveTo(x=1349, y=490)
    gui.press('q')
    gui.moveTo(x,y)
    gui.leftClick()

