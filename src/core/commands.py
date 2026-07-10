from datetime import datetime

from core.router import route
from tools.manager import ToolManager

tool_manager = ToolManager()


def execute(command):

    data = route(command)

    print("Router Output:", data)

    action = data.get("action")

    if action == "exit":
        return "exit"

    if action == "time":
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"

    result = tool_manager.execute(action, data)

    if result is not None:
        return result

    return "I don't know how to do that."