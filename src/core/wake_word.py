from core.listener import listen

WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "okay jarvis"
]


def wait_for_wake_word():

    print("💤 Waiting for wake word...")

    while True:

        text = listen()

        if not text:
            continue

        text = text.lower().strip()

        for wake in WAKE_WORDS:

            if text.startswith(wake):

                # Remove the wake word
                command = text[len(wake):].strip()

                # User only said "Jarvis"
                if command == "":
                    return None

                # User said "Jarvis open vscode"
                return command