from memory.manager import MemoryManager

memory = MemoryManager()


class MemoryTool:

    def execute(self, action, data):

        if action == "remember":

            return memory.remember(
                data["key"],
                data["value"]
            )

        elif action == "recall":

            value = memory.recall(data["key"])

            if value:
                return f"Your {data['key']} is {value}."

            return f"I don't know your {data['key']}."

        elif action == "forget":

            if memory.forget(data["key"]):
                return f"I forgot your {data['key']}."

            return f"I don't know your {data['key']}."

        return None