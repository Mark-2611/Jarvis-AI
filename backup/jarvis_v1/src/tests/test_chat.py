import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from services.ai import ask_gemini

print("===== JARVIS CHAT TEST =====")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    print("\nJarvis:")
    print(ask_gemini(question))