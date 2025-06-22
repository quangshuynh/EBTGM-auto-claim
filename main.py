import time
import pyautogui
import os


CLAIM_IMG = os.path.join(os.path.dirname(__file__), 'claim.png')
STAR_IMG  = os.path.join(os.path.dirname(__file__), 'star.png')


for path in (CLAIM_IMG, STAR_IMG):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Can't find {path} – make sure your PNG lives next to main.py")
CONFIDENCE = 0.75  

print("Switch to your game in 3 seconds…")
time.sleep(3)

while True:
    # 1. Try to find & click the green CLAIM button
    claim_xy = pyautogui.locateCenterOnScreen(CLAIM_IMG, confidence=CONFIDENCE)
    if claim_xy:
        pyautogui.click(claim_xy)
        print(f"[+] Clicked CLAIM at {claim_xy}")
        time.sleep(1)         
        continue              

    # 2. If no CLAIM found, look for the star icon to open the window
    star_xy = pyautogui.locateCenterOnScreen(STAR_IMG, confidence=CONFIDENCE)
    if star_xy:
        pyautogui.click(star_xy)
        print(f"[+] Opened level window by clicking STAR at {star_xy}")
        time.sleep(1)

    # 3. Wait a bit before scanning again
    time.sleep(5)
