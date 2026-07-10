import winsound

from core.listener import listen
from core.commands import execute
from core.speaker import speak
from core.wake_word import wait_for_wake_word

print("=" * 40)
print("        JARVIS AI")
print("=" * 40)

speak("Jarvis is online.")

while True:

    # Wait until user says "Jarvis"
    wait_for_wake_word()

    # Short confirmation beep
    winsound.Beep(1200, 120)

    # Listen for the actual command
    command = listen()

    if not command:
        continue

    response = execute(command)

    if response == "exit":
        speak("Goodbye!")
        break

    speak(response)