import pyautogui
import time

message = 1000
x = 0

while message >= 0:
    time.sleep(1)
    pyautogui.typewrite("Hello World🙂", interval=x)
    pyautogui.press('enter')
    message = message-1
    x += 1
