from core.listener import listen
from core.commands import execute
from core.speaker import speak

print("=" * 40)
print("      JARVIS VOICE TEST")
print("=" * 40)

speak("Jarvis is online.")

while True:

    command = listen()

    if not command:
        continue

    response = execute(command)

    if response == "exit":
        speak("Goodbye!")
        break


    speak(response)
    