import re


def route(command):

    command = command.lower().strip()

    # -----------------------------
    # Exit
    # -----------------------------

    if command in ["exit", "quit", "goodbye", "stop"]:

        return {
            "action": "exit"
        }

    # -----------------------------
    # Time
    # -----------------------------

    if "time" in command:

        return {
            "action": "time"
        }

    # -----------------------------
    # Remember
    # -----------------------------

    match = re.search(r"remember my (.+?) is (.+)", command)

    if match:

        return {
            "action": "remember",
            "key": match.group(1).strip(),
            "value": match.group(2).strip()
        }

    # -----------------------------
    # Recall
    # -----------------------------

    match = re.search(r"(what is|what's|whats) my (.+)", command)

    if match:

        return {
            "action": "recall",
            "key": match.group(2).strip()
        }

    # -----------------------------
    # Forget
    # -----------------------------

    match = re.search(r"forget my (.+)", command)

    if match:

        return {
            "action": "forget",
            "key": match.group(1).strip()
        }

    # -----------------------------
    # Google Search
    # -----------------------------

    if command.startswith("search google for"):

        return {
            "action": "google_search",
            "target": command.replace(
                "search google for",
                ""
            ).strip()
        }

    # -----------------------------
    # YouTube Search
    # -----------------------------

    if command.startswith("search youtube for"):

        return {
            "action": "youtube_search",
            "target": command.replace(
                "search youtube for",
                ""
            ).strip()
        }

    # -----------------------------
    # Open Website / Application
    # -----------------------------

    if command.startswith("open "):

        item = command.replace("open ", "").strip()

        websites = [
            "google",
            "youtube",
            "github",
            "gmail",
            "chatgpt",
            "chat gpt",
            "instagram",
            "facebook",
            "linkedin",
            "spotify",
            "amazon",
            "netflix",
        ]

        if item in websites:

            return {
                "action": "open_website",
                "target": item
            }

        return {
            "action": "open_app",
            "target": item
        }

    # -----------------------------
    # AI
    # -----------------------------

    return {
        "action": "chat",
        "target": command
    }