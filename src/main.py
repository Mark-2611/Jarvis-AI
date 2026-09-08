import os
import winsound

from core.listener import listen, listen_confirmation
from core.commands import execute
from core.speaker import speak
from core.wake_word import wait_for_wake_word, normalize_command


# =====================================================
# JARVIS STARTUP
# =====================================================

print("=" * 40)
print("        JARVIS AI")
print("=" * 40)

speak("Jarvis is online.")


# =====================================================
# Voice Confirmation Helper
# =====================================================

def get_confirmation():

    yes_words = [
        "yes",
        "yeah",
        "yep",
        "yup",
        "sure",
        "confirm",
        "confirmed",
        "do it",
        "delete it",
        "yes delete",
        "yes delete it",
        "go ahead",
        "okay",
        "ok",
    ]

    no_words = [
        "no",
        "nope",
        "nah",
        "cancel",
        "cancel it",
        "don't",
        "do not",
    ]

    for attempt in range(3):

        answer = normalize_command(
            listen_confirmation()
        )

        if not answer:

            speak(
                "I didn't hear you. "
                "Please say yes or no."
            )

            continue

        answer = answer.lower().strip()

        print(
            f"DEBUG CONFIRMATION: {answer!r}"
        )

        # -----------------------------
        # YES
        # -----------------------------

        if answer in yes_words:
            return True

        # -----------------------------
        # NO
        # -----------------------------

        if answer in no_words:
            return False

        # -----------------------------
        # Longer YES phrases
        # -----------------------------

        if (
            "yes" in answer
            or "yeah" in answer
            or "yep" in answer
            or "yup" in answer
            or "confirm" in answer
            or "do it" in answer
            or "delete it" in answer
            or "go ahead" in answer
        ):

            return True

        # -----------------------------
        # Longer NO phrases
        # -----------------------------

        if (
            "no" in answer
            or "nope" in answer
            or "cancel" in answer
            or "don't" in answer
            or "do not" in answer
        ):

            return False

        speak(
            "Please say yes or no."
        )

    return False


# =====================================================
# Voice Choice Helper
# =====================================================

def get_voice_choice(answer):

    if not answer:
        return None

    answer = answer.lower().strip()

    numbers = {

        "one": 1,
        "first": 1,
        "1": 1,

        "two": 2,
        "second": 2,
        "2": 2,

        "three": 3,
        "third": 3,
        "3": 3,

        "four": 4,
        "fourth": 4,
        "4": 4,

        "five": 5,
        "fifth": 5,
        "5": 5,
    }

    # ---------------------------------
    # Exact match
    # ---------------------------------

    if answer in numbers:

        return numbers[answer]

    # ---------------------------------
    # Handle phrases
    #
    # "number 2"
    # "number two"
    # "the second one"
    # "second one"
    # ---------------------------------

    for word, number in numbers.items():

        if (
            f"number {number}" in answer
            or f"number {word}" in answer
            or f"{word} one" in answer
            or f"the {word}" in answer
            or answer.startswith(f"{word} ")
        ):

            return number

    return None


# =====================================================
# Main Jarvis Loop
# =====================================================

while True:

    # ---------------------------------
    # Wait for wake word
    # ---------------------------------

    command = wait_for_wake_word()

    print(
        f"DEBUG COMMAND: {command!r}"
    )

    # ---------------------------------
    # User only said "Jarvis"
    # ---------------------------------

    if command is None:

        winsound.Beep(
            1200,
            120
        )

        command = normalize_command(
            listen()
        )

    if not command:
        continue

    # =================================================
    # Active Conversation
    # =================================================

    while True:

        response = execute(command)

        # =============================================
        # Exit
        # =============================================

        if response == "exit":

            speak("Goodbye!")

            exit()

        # =============================================
        # Dictionary Response
        # =============================================

        if isinstance(response, dict):

            status = response.get("status")

            # =========================================
            # Choose Chrome Profile
            # =========================================

            if status == "choose_chrome_profile":

                from services.browser import (
                    open_chrome_profile
                )

                speak(
                    "I found two Chrome profiles."
                )

                # -----------------------------
                # Profile 1
                # -----------------------------

                print(
                    "Number 1: Person 1"
                )

                speak(
                    "Number 1, Person 1"
                )

                # -----------------------------
                # Profile 2
                # -----------------------------

                print(
                    "Number 2: Mark 1"
                )

                speak(
                    "Number 2, Mark 1"
                )

                speak(
                    "Which Chrome profile "
                    "would you like to open?"
                )

                answer = normalize_command(
                    listen()
                )

                # -----------------------------
                # Person 1
                # -----------------------------

                if (
                    "person 1" in answer
                    or "person one" in answer
                ):

                    result = open_chrome_profile(
                        "person 1"
                    )

                    speak(result)

                # -----------------------------
                # Mark 1
                # -----------------------------

                elif (
                    "mark 1" in answer
                    or "mark one" in answer
                ):

                    result = open_chrome_profile(
                        "mark 1"
                    )

                    speak(result)

                # -----------------------------
                # Number selection
                # -----------------------------

                else:

                    choice = get_voice_choice(
                        answer
                    )

                    if choice == 1:

                        result = open_chrome_profile(
                            "person 1"
                        )

                        speak(result)

                    elif choice == 2:

                        result = open_chrome_profile(
                            "mark 1"
                        )

                        speak(result)

                    else:

                        speak(
                            "I didn't understand "
                            "your choice."
                        )

            # =========================================
            # Confirm Delete
            # =========================================

            elif status == "confirm_delete":

                from services.file_manager import (
                    perform_delete
                )

                target = response["target"]

                speak(
                    f"Are you sure you want to delete "
                    f"{target.name}?"
                )

                # IMPORTANT:
                # Use voice confirmation

                confirmed = get_confirmation()

                if confirmed:

                    result = perform_delete(
                        target
                    )

                    speak(result)

                else:

                    speak(
                        "Deletion cancelled."
                    )

            # =========================================
            # Choose Folder
            # =========================================

            elif status == "choose_folder":

                matches = response["matches"]

                speak(
                    f"I found {len(matches)} folders."
                )

                # -----------------------------
                # Show paths in terminal
                # Speak only numbers
                # -----------------------------

                for i, folder in enumerate(
                    matches,
                    start=1
                ):

                    print(
                        f"Number {i}: {folder}"
                    )

                    speak(
                        f"Number {i}"
                    )

                speak(
                    "Which one would you like "
                    "to open?"
                )

                answer = normalize_command(
                    listen()
                )

                choice = get_voice_choice(
                    answer
                )

                if (
                    choice
                    and choice <= len(matches)
                ):

                    os.startfile(
                        matches[choice - 1]
                    )

                    speak(
                        f"Opening folder number "
                        f"{choice}."
                    )

                else:

                    speak(
                        "I didn't understand "
                        "your choice."
                    )

            # =========================================
            # Choose Delete
            # =========================================

            elif status == "choose_delete":

                matches = response["matches"]

                speak(
                    f"I found {len(matches)} items."
                )

                # -----------------------------
                # Show paths in terminal
                # Speak only numbers
                # -----------------------------

                for i, item in enumerate(
                    matches,
                    start=1
                ):

                    print(
                        f"Number {i}: {item}"
                    )

                    speak(
                        f"Number {i}"
                    )

                speak(
                    "Which one would you like "
                    "to delete?"
                )

                answer = normalize_command(
                    listen()
                )

                choice = get_voice_choice(
                    answer
                )

                if (
                    choice
                    and choice <= len(matches)
                ):

                    target = matches[
                        choice - 1
                    ]

                    speak(
                        f"Are you sure you want "
                        f"to delete {target.name}?"
                    )

                    # IMPORTANT:
                    # Use voice confirmation

                    confirmed = get_confirmation()

                    if confirmed:

                        from services.file_manager import (
                            perform_delete
                        )

                        result = perform_delete(
                            target
                        )

                        speak(result)

                    else:

                        speak(
                            "Deletion cancelled."
                        )

                else:

                    speak(
                        "I didn't understand "
                        "your choice."
                    )

            # =========================================
            # Choose Rename
            # =========================================

            elif status == "choose_rename":

                matches = response["matches"]

                new_name = response[
                    "new_name"
                ]

                speak(
                    f"I found {len(matches)} "
                    f"matching items."
                )

                # -----------------------------
                # Show paths in terminal
                # Speak only numbers
                # -----------------------------

                for i, item in enumerate(
                    matches,
                    start=1
                ):

                    print(
                        f"Number {i}: {item}"
                    )

                    speak(
                        f"Number {i}"
                    )

                speak(
                    "Which one would you like "
                    "to rename?"
                )

                answer = normalize_command(
                    listen()
                )

                choice = get_voice_choice(
                    answer
                )

                if (
                    choice
                    and choice <= len(matches)
                ):

                    target = matches[
                        choice - 1
                    ]

                    try:

                        new_path = (
                            target.parent
                            / new_name
                        )

                        target.rename(
                            new_path
                        )

                        speak(
                            f"Renamed "
                            f"{target.name} "
                            f"to {new_name}."
                        )

                    except Exception as e:

                        speak(
                            f"Error renaming: {e}"
                        )

                else:

                    speak(
                        "I didn't understand "
                        "your choice."
                    )

            # =========================================
            # Unknown Dictionary Response
            # =========================================

            else:

                speak(
                    "I don't know how to "
                    "handle that response."
                )

        # =============================================
        # Normal Response
        # =============================================

        else:

            speak(response)

        # =============================================
        # Wait for next command
        # =============================================

        print(
            "👂 Waiting for another command..."
        )

        command = normalize_command(
            listen()
        )

        # ---------------------------------------------
        # User stopped speaking
        # ---------------------------------------------

        if not command:

            print(
                "💤 Going back to sleep...\n"
            )

            break