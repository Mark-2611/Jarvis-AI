import pyttsx3

def speak(text):
    engine = pyttsx3.init(driverName="sapi5")

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    print(f"Jarvis: {text}")

    engine.say(text)
    engine.runAndWait()
    engine.stop()