from PIL import ImageGrab , ImageOps
import pyautogui , time
from numpy import *

class coordinate():
    restartBtn = (600,400)
    dino = (360,400)
    box_left = (507,390)
    box_right = (557,431)

def restartGame():
    time.sleep(1)
    pyautogui.doubleClick(coordinate.restartBtn)
    print("Game is restarting...")

def jump():
    pyautogui.press("space")
    print("DINO:JUMP")

def imagegrab():
    #box = coordinate.box_left + coordinate.box_right
    #box = convert_view(box)
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    s = array(image.getcolors()).sum()
    return s


def bot_play():
    while True:
        x = imagegrab()
        print(x)
        if (x != 8447):
            jump()

def test():
    time.sleep(1)
    pyautogui.moveTo(coordinate.box_left)
    time.sleep(1)
    pyautogui.moveTo(coordinate.box_right)

def save_box(count):
    #box = coordinate.box_left + coordinate.box_right
    #box = (387,390,437,429)
    #box = convert_view(box)
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    s = array(image).sum()
    color = array(image.getcolors()).sum()
    image.save("vision" + str(count) + ".jpeg" , "JPEG")
    print("- SAVED -" + str(count) + "<<<" + str(color) + ">>>" + str(s))


def convert_view(b):
    t = tuple()
    for i in range(len(b)):
        t = t + (b[i]*2,)
    return t

#test()
global box
box = coordinate.box_left + coordinate.box_right
box = convert_view(box)

restartGame()
bot_play()

"""
restartGame()
time.sleep(4)
for i in range(20):
    save_box(i+1)
"""

