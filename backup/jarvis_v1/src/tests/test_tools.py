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

from tools.manager import ToolManager

manager = ToolManager()

print("=" * 40)
print("      TOOL MANAGER TEST")
print("=" * 40)

tests = [

    {
        "action": "remember",
        "key": "college",
        "value": "GTU"
    },

    {
        "action": "recall",
        "key": "college"
    },

    {
        "action": "open_app",
        "target": "vscode"
    },

]

for test in tests:

    action = test["action"]

    print()

    print("Action:", action)

    print(manager.execute(action, test))