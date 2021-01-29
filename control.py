import time
import pyautogui

for _ in range(3):
    time.sleep(1)
    pyautogui.moveTo(100, 100, duration=0.5)
    pyautogui.click(1000, 110, duration=0.5)
    pyautogui.typewrite('I Done!!!!')


