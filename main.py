import time
import pyautogui              
import pydirectinput as pd    

CLOSE_CX, CLOSE_CY = 1690, 414 # center of window close button

# 100px diameter around the close button
BOX_SIZE = 100 
REGION = (CLOSE_CX - BOX_SIZE // 2, CLOSE_CY - BOX_SIZE // 2, BOX_SIZE, BOX_SIZE)

OPEN_BUTTON   = [(84, 1027), (85, 1028)]
CLAIM_BUTTONS = [
    (1452, 788), # 5xp
    (1295, 780), # 10xp 
    #(1104, 791), # 30xp
    #(951,  784), # 100xp
    #(1053, 151) # save to bank
    ]
INTERVAL      = 3.0    

pyautogui.FAILSAFE = False
pd.FAILSAFE       = False
pd.PAUSE         = 0.05

def is_window_up() -> bool:
    img = pyautogui.screenshot(region=REGION)
    for r, g, b in img.getdata():
        if r > 200 and g < 80 and b < 80:
            return True
    return False

def start_txt():
    for i in range(3, 0, -1):
        print(f"  Starting in {i}s…")
        time.sleep(1)
    print(" Auto-claimer running! Ctrl-C to stop")

def move_click():
    while True:
        if not is_window_up():  # open level window
            print(f"[{time.strftime('%H:%M:%S')}] level window closed → opening")
            for i, pos in enumerate(OPEN_BUTTON, 1):
                pd.moveTo(*pos)
                pd.click()
        else: # claim rewards
            print(f"[{time.strftime('%H:%M:%S')}] level window open → claiming")
            for i, pos in enumerate(CLAIM_BUTTONS, 1):
                pd.moveTo(*pos) # move to button
                time.sleep(0.1)             
                pd.click() # first click
                time.sleep(0.2) 
                pd.click() # second click
                print(f"  • double-clicked #{i} at {pos}")
                time.sleep(0.5)               
        time.sleep(INTERVAL)

def main():
    start_txt()
    move_click()

if __name__ == "__main__":
    main()
