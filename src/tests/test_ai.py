from src.skills.ai import ask_gemini

while True:

    question = input("You: ").strip()

    if not question:
        continue

    if question.lower() == "exit":
        break

    answer = ask_gemini(question)

    print("\nGemini:\n")
    print(answer)
    print()