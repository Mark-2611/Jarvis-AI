import winsound

from core.listener import listen
from core.commands import execute
from core.speaker import speak
from core.wake_word import wait_for_wake_word, normalize_command

print("=" * 40)
print("        JARVIS AI")
print("=" * 40)

speak("Jarvis is online.")

while True:

    # Wait for wake word
    command = wait_for_wake_word()
    print(f"DEBUG COMMAND: {command!r}")

    # User only said "Jarvis"
    if command is None:

        winsound.Beep(1200, 120)

        command = normalize_command(listen())

    if not command:
        continue

    while True:

        response = execute(command)

        if response == "exit":
            speak("Goodbye!")
            exit()

        speak(response)

        print("👂 Waiting for another command...")

        command = normalize_command(listen())

        # User stopped speaking
        if not command:

            print("💤 Going back to sleep...\n")

            break