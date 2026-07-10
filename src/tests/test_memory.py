import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from memory.manager import MemoryManager


memory = MemoryManager()

print(memory.remember("name", "Mark"))

print(memory.recall("name"))

print(memory.list_memory())