import time
import pyautogui

from core.listener import listen
from core.speaker import speak
from core.wake_word import normalize_command

from utils.window_manager import focus_last_window


def start_dictation():

    speak("Dictation mode started.")

    # Automatically switch back to the last opened application
    if focus_last_window():
        print("Focused last application.")
    else:
        print("Could not focus last application.")

    time.sleep(0.5)

    while True:

        text = normalize_command(listen())

        if not text:
            continue

        text = text.lower().strip()

        print("DICTATION:", text)

        if text in [
            "stop dictation",
            "stop",
            "exit",
            "quit",
            "cancel",
        ]:
            speak("Dictation stopped.")
            break

        elif text == "new line":
            pyautogui.press("enter")

        elif text == "new paragraph":
            pyautogui.press("enter")
            pyautogui.press("enter")

        elif text == "tab":
            pyautogui.press("tab")

        elif text == "backspace":
            pyautogui.press("backspace")

        else:
            pyautogui.write(text + " ", interval=0.02)