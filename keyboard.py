import os
from time import sleep
import pyautogui
import keyboard as k
'''
pip install pyautogui
pip install keyboard
'''
cwd = os.getcwd()
h = open("haa.bat" , "w+")
matn = '''@echo off
color 0a
Mode Con Cols=300 Lines=100

:a
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto a'''
h.write(matn)
h.close()
a = 0
b = 0
def onpress(key):
    global a
    if k.is_pressed("c") and b == 1:
        ma = "\n\n\n\n\n\n\n\nba bay :))))"
        k.write(ma, delay=0.1)
        sleep(0.5)
        pyautogui.hotkey("alt", "f4")
        sleep(0.3)
        k.press_and_release("right")
        k.press_and_release("enter")
        sleep(0.3)
        k.press_and_release("left windows + R")
        sleep(0.3)
        k.write("cmd")
        k.press_and_release("enter")
        sleep(0.3)
        k.write("taskkill /im cmd.exe")
        k.press_and_release("enter")
        sleep(0.3)
        f = os.path.join(cwd ,"haa.bat")
        os.remove(f)
        sleep(0.3)
        a = 1
    else:
        k.press("backspace")
k.on_press(onpress) 
k.press_and_release("left windows + R")
sleep(0.2)
k.write("cmd")
k.press_and_release("enter")
sleep(0.3)
k.press_and_release("left windows + up")
k.write("cd "+cwd)
k.press_and_release("enter")
sleep(0.3)
k.write("haa.bat")
k.press_and_release("enter")
sleep(5)
k.press_and_release("left windows + R")
sleep(0.2)
k.write("notepad.exe")
k.press_and_release("enter")
sleep(0.5)

ma = "salam :)\nlotfan hich kari nakon\nbayad begam to hack shodi :)\n\n\n\n\nkeyboardet kar nemikone :)))))\n\n\n\n\n*** ALihackpy ***"
k.write(ma , delay=0.1)
c = 0

while True:
    if c == 0 :
        sleep(5)
        ma = "\n\n\n\n\n\n\n\ndelam barat misoze :)\n\n\n\n\n\n\n\ndokme 'c' ro feshar bede ta man beram"
        k.write(ma, delay=0.1)
        b = 1
        c = 1
    if a == 1 :
        break
    
