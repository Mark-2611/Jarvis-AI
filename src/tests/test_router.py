import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.router import route_command

print("=" * 40)
print("     JARVIS ROUTER TEST")
print("=" * 40)

while True:

    command = input("\nYou: ")

    if command.lower() == "exit":
        break

    result = route_command(command)

    print("\nRouter:")
    print(result)