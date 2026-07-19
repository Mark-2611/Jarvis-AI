class ConversationMemory:

    def __init__(self, max_history=10):

        self.max_history = max_history
        self.history = []

    def add(self, role, message):

        self.history.append({
            "role": role,
            "message": message
        })

        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_context(self):

        context = ""

        for item in self.history:

            context += f"{item['role']}: {item['message']}\n"

        return context

    def clear(self):

        self.history.clear()