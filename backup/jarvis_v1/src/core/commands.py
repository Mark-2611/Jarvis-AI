from datetime import datetime

from core.router import route
from tools.manager import ToolManager
from services.dictation import start_dictation

from services.browser import (
    open_chrome_profile,
    open_website_in_profile,
    google_search_in_profile,
)

tool_manager = ToolManager()


def execute(command):

    data = route(command)

    print("Router Output:", data)

    action = data.get("action")

    if action == "exit":
        return "exit"

    if action == "time":
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"
    elif action == "dictation":
        start_dictation()
        return "Done."
    elif action == "profile_open":

        return open_chrome_profile(
            data["profile"]
        )


    elif action == "profile_website":

        return open_website_in_profile(
        data["profile"],
        data["target"]
    )


    elif action == "profile_search":

        return google_search_in_profile(
        data["profile"],
        data["target"]
    )     

    result = tool_manager.execute(action, data)

    if result is not None:
        return result

    return "I don't know how to do that."