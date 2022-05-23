import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=316, y=481, clicks=2)
time.sleep(3)

pyautogui.write("youtube.com")
time.sleep(3)
#pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(10)

pyautogui.click(x=49, y=283, clicks=2)

time.sleep(3)

pyautogui.hotkey("ctrl", "t")
pyautogui.write("uol.com")
time.sleep(3)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=945, y=19, clicks=1)
time.sleep(2)
pyautogui.click(x=945, y=19, clicks=1)

# time.sleep(10)
# print(pyautogui.position())

