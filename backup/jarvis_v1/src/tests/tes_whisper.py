import speech_recognition as sr
from faster_whisper import WhisperModel

print("Loading Whisper model... (first time may take a minute)")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    recognizer.adjust_for_ambient_noise(source)

    print("\n🎤 Speak something...")

    audio = recognizer.listen(
    source,
    timeout=5,
    phrase_time_limit=8
    )

    with open("temp.wav", "wb") as f:
        f.write(audio.get_wav_data())

segments, info = model.transcribe(
    "temp.wav",
    language="en",
    beam_size=5
)
print("Detected language:", info.language)

print("\n===== WHISPER RESULT =====")

for segment in segments:
    print(segment.text)