import speech_recognition as sr

recognizer = sr.Recognizer()

# ==============================
# NORMAL LISTENER SETTINGS
# ==============================

recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1.2
recognizer.non_speaking_duration = 0.4

# Calibrate only once
calibrated = False


def calibrate(source):
    global calibrated

    if not calibrated:
        print("🎙️ Calibrating microphone...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        calibrated = True

        print("✅ Calibration complete.")


# ==============================
# NORMAL LISTEN
# ==============================

def listen():

    try:

        with sr.Microphone() as source:

            calibrate(source)

            print("🎤 Listening...")

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=20
            )

            print("🧠 Recognizing...")

            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            command = command.lower().strip()

            # Normalize common phrases
            replacements = {
                "vs code": "vscode",
                "visual studio": "visual studio code",
                "git hub": "github",
                "chat gp": "chatgpt",

                " dot ": ".",
                " underscore ": "_",
                " dash ": "-",
                " hyphen ": "-",
            }

            command = command.replace(" dot ", ".")
            command = command.replace(" underscore ", "_")
            command = command.replace(" dash ", "-")
            command = command.replace(" hyphen ", "-")

            for old, new in replacements.items():
                command = command.replace(old, new)

            print(f"Google heard: '{command}'")

            return command

    except sr.WaitTimeoutError:

        print("⌛ No speech detected.")
        return ""

    except sr.UnknownValueError:

        print("❌ Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:

        print("❌ Could not connect to Google Speech Recognition.")
        return ""

    except Exception as e:

        print(f"❌ Error: {e}")
        return ""


# ==============================
# CONFIRMATION LISTENER
# ==============================

def listen_confirmation():

    try:

        with sr.Microphone() as source:

            calibrate(source)

            print("🎤 Listening for confirmation...")

            # Give the user a little time to start speaking
            audio = recognizer.listen(
                source,
                timeout=8,
                phrase_time_limit=4
            )

            print("🧠 Recognizing confirmation...")

            answer = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            answer = answer.lower().strip()

            print(f"Google heard confirmation: '{answer}'")

            return answer

    except sr.WaitTimeoutError:

        print("⌛ No confirmation detected.")
        return ""

    except sr.UnknownValueError:

        print("❌ Couldn't understand confirmation.")
        return ""

    except sr.RequestError:

        print("❌ Could not connect to Google Speech Recognition.")
        return ""

    except Exception as e:

        print(f"❌ Confirmation error: {e}")
        return ""