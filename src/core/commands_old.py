from datetime import datetime
from skills.ai import ask_gemini

from skills.browser import (
    open_website,
    search_google,
    search_youtube,
)

from skills.system import open_application


def execute(command):

    # Greeting
    if "hello" in command:
        return "Hello! How can I help you?"

    # Time
    elif "time" in command:
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"

    # Google Search
    elif command.startswith("search google for"):
        query = command.replace("search google for", "").strip()

        if query:
            return search_google(query)

        return "What do you want me to search on Google?"

    # YouTube Search
    elif command.startswith("search youtube for"):
        query = command.replace("search youtube for", "").strip()

        if query:
            return search_youtube(query)

        return "What do you want me to search on YouTube?"

    # Open Websites or Applications
    elif command.startswith("open "):

        item = command.replace("open ", "").strip()

        websites = [
            "google",
            "youtube",
            "github",
            "gmail",
            "chat gpt",
            "chatgpt",
            "instagram",
            "facebook",
            "linkedin",
            "spotify",
            "amazon",
            "netflix",
        ]

        if item in websites:
            return open_website(item)

        return open_application(item)

    # Exit
    elif any(word in command for word in [
        "exit",
        "quit",
        "goodbye",
        "close jarvis",
        "stop"
    ]):
        return "exit"

    # Unknown command → Ask Gemini
    else:
        return ask_gemini(command)