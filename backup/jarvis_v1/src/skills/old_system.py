import subprocess

# ------------------------
# Simple Windows Apps
# ------------------------

def open_notepad():
    subprocess.Popen("notepad")
    return "Opening Notepad."


def open_calculator():
    subprocess.Popen("calc")
    return "Opening Calculator."


def open_paint():
    subprocess.Popen("mspaint")
    return "Opening Paint."


def open_cmd():
    subprocess.Popen("cmd")
    return "Opening Command Prompt."


def open_explorer():
    subprocess.Popen("explorer")
    return "Opening File Explorer."


# ------------------------
# Installed Applications
# ------------------------

APPS = {

    # Browsers
    "chrome": "chrome",
    "edge": "msedge",
    "firefox": "firefox",

    # Code Editors
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",

    # Music
    "spotify": "spotify",

    # Communication
    "discord": "discord",
    "telegram": "telegram",
    "whatsapp": "whatsapp",

    # Gaming
    "steam": "steam",

    # Microsoft Office
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
}


def open_application(app):

    app = app.lower().strip()

    if app not in APPS:
        return f"I don't know how to open {app}."

    try:
        # shell=True is needed because commands like "code"
        # are actually Windows .cmd files.
        subprocess.Popen(APPS[app], shell=True)
        return f"Opening {app}."

    except Exception as e:
        return f"ERROR: {e}"