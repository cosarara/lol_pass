import pyautogui
import cv2
import numpy as np
import time
import subprocess

def main():
    subprocess.Popen(["league_nopass"])
    time.sleep(15) # wait for league to start

    with open('pass.txt') as f:
        pwd = f.readline()

    template = cv2.imread('pass.png')
    h, w = template.shape[:2]

    for i in range(10):
        screen_rgb = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen_rgb), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screen, template, cv2.TM_CCORR_NORMED)
        (_, conf, _, loc) = cv2.minMaxLoc(result)
        print('confidence:', conf)
        if conf < 0.9:
            time.sleep(2)
            continue
        x, y = loc
        x += w / 2
        y += h / 2
        print(x, y)
        break
    else:
        print('giving up!')
        return

    pyautogui.click(x, y)
    pyautogui.typewrite(pwd+'\n', interval=0.05)

if __name__ == "__main__":
    main()
