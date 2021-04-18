from PIL import ImageOps , Image
from numpy import *
import pyautogui as pag
import mss
import mss.tools
import mss.screenshot
import time

#position is 1280 x 800
#result image is 2560 x 1600


class xy:
    restart_btn = (375,395)
    dino = (140,400)
    box_start = (200,400)
    box_end = (240,430)


def restart():
    pag.doubleClick(xy.restart_btn)
    print("Restarting...")
    pag.click((375,250))


def jump():
    pag.press("up")
    print("DINO : jump")


def isdead(a):
    global end_game
    if len(end_game) < 100:
        end_game.append(a)
    else:
        if len(set(end_game)) == 1:
            print("DINO : dead")
            print("DINO : survived",time.time() - start_time)
            exit()
        else:
            end_game = []


def one_sec():
    global fps_timer
    if time.time() - fps_timer >= 1:
        return True
    else:
        return False


def fps_reset():
    global fps , fps_timer
    print("FPS :" , fps)
    fps = 0
    fps_timer = time.time()


def level():
    global start_time
    t = time.time() - start_time
    if t > 180:
        current_level = 4
        return int(current_level)
    else:
        current_level = t//45
        return int(current_level)


def vision():
    global monitor , refresh_rate
    global fps

    with mss.mss() as sct:
        time.sleep(refresh_rate[lv])
        mon = monitor[lv]
        img = sct.grab(mon)
        img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        img = ImageOps.grayscale(img)
        a = array(img.getcolors()).sum()

    isdead(a)
    fps += 1
    return a



monitor = [
    {'left': 210, 'top': 400, 'width': 40, 'height': 25} ,
    {'left': 230, 'top': 400, 'width': 40, 'height': 25} ,
    {'left': 250, 'top': 400, 'width': 60, 'height': 25} ,
    {'left': 270, 'top': 400, 'width': 60, 'height': 25}
]

refresh_rate = [0.03 , 0.02 , 0.01 , 0.005]

restart()
time.sleep(3)

fps = 0
end_game = []

start_time = time.time()
fps_timer = time.time()

while True:
    #fps display
    if one_sec():
        fps_reset()

    lv = level()

    #print(vision())
    if (vision() != 4247):
        jump()

