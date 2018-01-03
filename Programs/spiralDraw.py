# Spiral draw

import pyautogui
import time

time.sleep(5)
pyautogui.click()
distance = 200

def up():
    pyautogui.dragRel(0, -5,) #duration=0.2)
    pyautogui.dragRel(5, 0)
    pyautogui.dragRel(0, 5)


def right():
    pyautogui.dragRel(5, 0)
    pyautogui.dragRel(0, 5)
    pyautogui.dragRel(-5, 0)


def down():
    pyautogui.dragRel(0, 5)
    pyautogui.dragRel(-5, 0)
    pyautogui.dragRel(0, -5)


def left():
    pyautogui.dragRel(-5, 0)
    pyautogui.dragRel(0, -5)
    pyautogui.dragRel(5, 0)

while distance > 0:
    for i in range(distance//10):
        up()
        if i != range(distance//10)[-1]: # do not draw last line
            pyautogui.dragRel(5, 0)
    distance -= 10
    for i in range(distance//10):
        right()
        if i != range(distance//10)[-1]: # do not draw last line
            pyautogui.dragRel(0, 5)
    for i in range(distance//10):
        down()
        if i != range(distance//10)[-1]: # do not draw last line
            pyautogui.dragRel(-5, 0)
    distance -= 10
    for i in range(distance//10):
        left()
        if i != range(distance//10)[-1]: # do not draw last line
            pyautogui.dragRel(0, -5)