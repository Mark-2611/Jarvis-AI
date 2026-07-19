from google import genai
from config.settings import GEMINI_API_KEY
from memory.conversation import ConversationMemory

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Create conversation memory
conversation = ConversationMemory()


def ask_gemini(prompt):

    try:

        # Save user's message
        conversation.add("User", prompt)

        # Build conversation context
        context = conversation.get_context()

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=context
        )

        answer = response.text

        # Save Jarvis response
        conversation.add("Jarvis", answer)

        return answer

    except Exception as e:

        error = str(e).lower()

        if "429" in error or "quota" in error:
            return "My AI quota has been reached. Please try again later."

        if "503" in error or "unavailable" in error:
            return "Gemini is busy right now. Please try again in a moment."

        return f"Gemini Error: {e}"