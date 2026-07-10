import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from memory.conversation import ConversationMemory

memory = ConversationMemory()

memory.add("User", "Who invented Python?")
memory.add("Jarvis", "Guido van Rossum.")

memory.add("User", "Where was he born?")

print(memory.get_context())