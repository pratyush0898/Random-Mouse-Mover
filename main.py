import pyautogui as pag
import random
import time
import sys

print("Press ctrl + C to quit anytime")

try:
    while True: 
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, 0.9)
        time.sleep(0)
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
