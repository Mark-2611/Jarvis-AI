from core.listener import listen

WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "okay jarvis"
]


def normalize_command(command):
    if not command:
        return command

    command = command.lower().strip()

    for wake in WAKE_WORDS:
        if command.startswith(wake):
            return command[len(wake):].strip()

    return command


def wait_for_wake_word():

    print("💤 Waiting for wake word...")

    while True:

        text = listen()

        if not text:
            continue

        text = text.lower().strip()

        for wake in WAKE_WORDS:

            if text.startswith(wake):

                command = text[len(wake):].strip()

                if command == "":
                    return None

                return command