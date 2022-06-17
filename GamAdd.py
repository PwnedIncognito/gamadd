import pyautogui as pt
from time import sleep
import pyperclip
import random

print("-Welcome to GamAdd 1.0-")
input("Press Enter to continue...")
print("Good luck!")
sleep(5)
position = pt.locateOnScreen("enter_code.png", confidence=.6)
x = position[0]
y = position[1]


def entercode():
    global x, y
    random_sufix = random.randint(100000000, 999999999)
    code = "010100331152531906220256" + str(random_sufix)
    print(code)
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 80, y + 70, duration=.5)
    pt.click()
    pt.typewrite(code)
    pt.moveTo(x + 600, y + 80, duration=.5)
    pt.click()
    sleep(10)
    position_okay = pt.locateOnScreen("okay.png", confidence=.6)
    x_okay = position_okay[0]
    y_okay = position_okay[1]
    pt.moveTo(x_okay, y_okay, duration=.5)
    pt.click()

while True:
    entercode()
