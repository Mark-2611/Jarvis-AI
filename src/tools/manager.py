from .browser_tool import BrowserTool
from .system_tool import SystemTool
from .memory_tool import MemoryTool
from .chat_tool import ChatTool


class ToolManager:

    def __init__(self):

        self.tools = [
            BrowserTool(),
            SystemTool(),
            MemoryTool(),
            ChatTool()
        ]

    def execute(self, action, data):

        for tool in self.tools:

            result = tool.execute(action, data)

            if result is not None:
                return result

        return None