import speech_recognition as sr

recognizer = sr.Recognizer()

# Configure once
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.5

# Calibrate only once
calibrated = False


def listen():

    global calibrated

    try:

        with sr.Microphone() as source:

            # Calibrate only on the first run
            if not calibrated:

                print("🎙️ Calibrating microphone...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                calibrated = True

                print("✅ Calibration complete.")

            print("🎤 Listening...")

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
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
            }

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