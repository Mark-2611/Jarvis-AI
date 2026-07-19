import json
import os


class MemoryManager:

    def __init__(self):

        self.memory_file = os.path.join(
            os.path.dirname(__file__),
            "memory.json"
        )

        self.memory = self.load()

    # -----------------------
    # Load Memory
    # -----------------------

    def load(self):

        if not os.path.exists(self.memory_file):

            return {
                "profile": {},
                "preferences": {},
                "conversation": []
            }

        try:

            with open(self.memory_file, "r") as file:

                return json.load(file)

        except:

            return {
                "profile": {},
                "preferences": {},
                "conversation": []
            }

    # -----------------------
    # Save Memory
    # -----------------------

    def save(self):

        with open(self.memory_file, "w") as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

    # -----------------------
    # Profile Memory
    # -----------------------

    def remember(self, key, value):

        self.memory["profile"][key] = value

        self.save()

        return f"I'll remember your {key}."

    def recall(self, key):

        return self.memory["profile"].get(key)

    def forget(self, key):

        if key in self.memory["profile"]:

            del self.memory["profile"][key]

            self.save()

            return True

        return False

    # -----------------------
    # Conversation Memory
    # -----------------------

    def add_message(self, role, message):

        self.memory["conversation"].append({

            "role": role,
            "message": message

        })

        # Keep only last 20 messages

        self.memory["conversation"] = \
            self.memory["conversation"][-20:]

        self.save()

    def get_conversation(self):

        return self.memory["conversation"]

    # -----------------------
    # Show All Memory
    # -----------------------

    def show(self):

        return self.memory