from services.ai import ask_gemini


class ChatTool:

    def execute(self, action, data):

        if action != "chat":
            return None

        return ask_gemini(data["target"])