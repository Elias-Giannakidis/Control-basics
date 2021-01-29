import pygetwindow
import pyautogui
from PIL import Image
import time

path = '/Users/EGiannakidis/Desktop/MyProjects/Python/Take Screenshot/screenshot'

windows = pygetwindow.getAllWindows()
for win in windows:
    if win.title == 'AVOID ENEMIES':
        myWin = win

for i in range(15):
    time.sleep(1)
    x1 = int(myWin.left)
    y1 = int(myWin.top)
    width = int(myWin.width)
    height = int(myWin.height)
    x2 = x1 + width
    y2 = y1 + height
    if x1 > 0:
        pyautogui.screenshot(path+".png")
        img = Image.open(path+".png")
        img = img.crop((x1, y1, x2, y2))
        img.save(path+str(i)+".png")