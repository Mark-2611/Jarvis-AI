import os
import subprocess

START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
]


def discover_shortcuts():
    apps = {}

    for base in START_MENU_PATHS:

        if not os.path.exists(base):
            continue

        for root, _, files in os.walk(base):

            for file in files:

                if file.endswith(".lnk"):

                    name = os.path.splitext(file)[0].lower()

                    apps[name] = {
                        "type": "shortcut",
                        "path": os.path.join(root, file)
                    }

    return apps


def discover_store_apps():
    apps = {}

    try:
        result = subprocess.run(
            [
                "powershell",
                "-Command",
                "Get-StartApps | Select-Object Name,AppID"
            ],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        lines = result.stdout.splitlines()

        for line in lines[3:]:   # Skip header

            parts = line.strip().split()

            if len(parts) < 2:
                continue

            appid = parts[-1]
            name = " ".join(parts[:-1]).lower()

            apps[name] = {
                "type": "store",
                "id": appid
            }

    except Exception as e:
        print("Store app discovery failed:", e)

    return apps


def discover_apps():

    apps = {}

    apps.update(discover_shortcuts())
    apps.update(discover_store_apps())

    return apps