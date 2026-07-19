import os
import subprocess
import time

from utils.app_discovery import discover_apps
from utils.window_manager import set_last_window

# Discover installed applications once
DISCOVERED_APPS = discover_apps()

print(f"Loaded {len(DISCOVERED_APPS)} applications")

# Aliases
ALIASES = {
    "vscode": "visual studio code",
    "vs code": "visual studio code",
    "visual studio": "visual studio code",

    "chrome": "google chrome",
    "google chrome": "google chrome",

    "cmd": "command prompt",
    "powershell": "windows powershell",

    "word": "word 2013",
    "excel": "excel 2013",
    "powerpoint": "powerpoint 2013",
}


# ------------------------
# Windows Built-in Apps
# ------------------------

def open_notepad():
    subprocess.Popen("notepad")
    set_last_window("Notepad")
    return "Opening Notepad."


def open_calculator():
    subprocess.Popen("calc")
    set_last_window("Calculator")
    return "Opening Calculator."


def open_paint():
    subprocess.Popen("mspaint")
    set_last_window("Paint")
    return "Opening Paint."


def open_cmd():
    subprocess.Popen("cmd")
    set_last_window("Command Prompt")
    return "Opening Command Prompt."


def open_explorer():
    subprocess.Popen("explorer")
    set_last_window("File Explorer")
    return "Opening File Explorer."


# ------------------------
# Launch Installed Apps
# ------------------------

def launch_app(info):
    """
    Launch either a desktop shortcut or a Microsoft Store app.
    """

    if info["type"] == "shortcut":
        os.startfile(info["path"])

    elif info["type"] == "store":
        subprocess.Popen(
            [
                "explorer.exe",
                f"shell:AppsFolder\\{info['id']}"
            ]
        )

    # Give Windows a moment to create the window
    time.sleep(1)


# ------------------------
# Open Application
# ------------------------

def open_application(app):

    app = app.lower().strip()

    # Apply aliases
    app = ALIASES.get(app, app)

    print(f"Searching for: {app}")

    # ------------------------
    # Exact Match
    # ------------------------

    if app in DISCOVERED_APPS:

        info = DISCOVERED_APPS[app]

        print("Found:", info)

        launch_app(info)

        # Remember the exact app name
        set_last_window(app)

        return f"Opening {app}."

    # ------------------------
    # Starts With Match
    # ------------------------

    for name, info in DISCOVERED_APPS.items():

        if name.startswith(app):

            print(f"Matched: {name}")

            launch_app(info)

            set_last_window(name)

            return f"Opening {name}."

    # ------------------------
    # Contains Match
    # ------------------------

    for name, info in DISCOVERED_APPS.items():

        if app in name:

            print(f"Matched: {name}")

            launch_app(info)

            set_last_window(name)

            return f"Opening {name}."

    return f"I couldn't find an installed application called {app}."