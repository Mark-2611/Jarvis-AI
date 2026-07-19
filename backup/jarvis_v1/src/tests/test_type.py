import time
import pyautogui

print("You have 5 seconds...")
time.sleep(5)

pyautogui.write("Hello from Jarvis!", interval=0.05)