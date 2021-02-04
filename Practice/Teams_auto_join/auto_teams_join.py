import pyautogui
import os
from datetime import datetime
import time


os.popen('teams')

# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

while True:
    hours = datetime.now().strftime("%H")
    minutes = datetime.now().strftime("%M")
    if not int(minutes) >= 30:
        time.sleep(240)
        continue
    if not int(hours) == 8:
        time.sleep(3600)
        continue
    day = datetime.now().strftime("%d")
    if int(day) > 4 or int(day) < 1: 
        time.sleep(86400)

    dsp_class = pyautogui.locateCenterOnScreen('DSP.png')
    time.sleep(1)
    pyautogui.moveTo(dsp_class)
    pyautogui.click()
    time.sleep(1)

    join = pyautogui.locateCenterOnScreen('join.png')
    time.sleep(1)
    if join == None:
        time.sleep(120)
        continue

    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(3)

    join_now = pyautogui.locateCenterOnScreen('join_now.png')
    time.sleep(1)
    pyautogui.moveTo(join_now)
    pyautogui.click()
    
    print("joined")
    time.sleep(1000)