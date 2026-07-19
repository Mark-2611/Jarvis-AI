import os
import sys

# Add the src folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from utils.app_discovery import discover_apps

apps = discover_apps()

print(f"\nFound {len(apps)} applications:\n")

for name in sorted(apps):
    print(name)