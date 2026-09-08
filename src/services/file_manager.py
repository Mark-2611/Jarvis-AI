import os
from pathlib import Path
import shutil
import subprocess


# =====================================================
# Create Folder
# =====================================================

def create_folder(folder_name):

    try:

        folder = Path.home() / folder_name

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return f"Folder '{folder_name}' created successfully."

    except Exception as e:

        return f"Error creating folder: {e}"


# =====================================================
# Create File
# =====================================================

def create_file(file_name):

    try:

        file = Path.home() / file_name

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.touch(
            exist_ok=True
        )

        return f"File '{file_name}' created successfully."

    except Exception as e:

        return f"Error creating file: {e}"


# =====================================================
# Find Matching Folders
# =====================================================

def get_matching_folders(folder_name):

    home = Path.home()

    common_locations = [

        home,
        home / "Desktop",
        home / "Documents",
        home / "Downloads",
        home / "Pictures",
        home / "Music",
        home / "Videos",

    ]

    matches = []

    for location in common_locations:

        if location.exists():

            for item in location.iterdir():

                if (
                    item.is_dir()
                    and
                    item.name.lower() == folder_name.lower()
                ):

                    matches.append(item)

    return matches


# =====================================================
# Open Folder
# =====================================================

def open_folder(folder_name):

    matches = get_matching_folders(folder_name)

    if len(matches) == 0:

        return f"No folder named '{folder_name}' found."

    if len(matches) == 1:

        os.startfile(matches[0])

        return f"Opening {matches[0].name}"

    return {
        "status": "choose_folder",
        "matches": matches
    }


# =====================================================
# Rename File / Folder
# =====================================================

def rename_item(old_name, new_name):

    try:

        home = Path.home()

        matches = []

        for item in home.rglob("*"):

            if item.name.lower() == old_name.lower():

                matches.append(item)

        if not matches:

            return f"I couldn't find '{old_name}'."

        if len(matches) == 1:

            target = matches[0]

            new_path = target.parent / new_name

            target.rename(new_path)

            return (
                f"Renamed '{old_name}' "
                f"to '{new_name}'."
            )

        return {
            "status": "choose_rename",
            "matches": matches,
            "new_name": new_name
        }

    except Exception as e:

        return f"Error: {e}"


# =====================================================
# Delete File / Folder
# =====================================================

def delete_item(name, item_type=None):

    home = Path.home()

    common_locations = [
        home,
        home / "Desktop",
        home / "Documents",
        home / "Downloads",
        home / "Pictures",
        home / "Music",
        home / "Videos",
    ]

    matches = []

    for location in common_locations:

        if not location.exists():
            continue

        try:

            for item in location.iterdir():

                if item.name.lower() != name.lower():
                    continue

                if item_type == "folder" and not item.is_dir():
                    continue

                if item_type == "file" and not item.is_file():
                    continue

                matches.append(item)

        except PermissionError:
            continue

    if not matches:

        if item_type == "folder":
            return f"I couldn't find folder '{name}'."

        elif item_type == "file":
            return f"I couldn't find file '{name}'."

        return f"I couldn't find '{name}'."

    if len(matches) == 1:

        return {
            "status": "confirm_delete",
            "target": matches[0]
        }

    return {
        "status": "choose_delete",
        "matches": matches
    }


# =====================================================
# Perform Delete
# =====================================================

def perform_delete(target):

    try:

        if target.is_dir():

            shutil.rmtree(target)

        else:

            target.unlink()

        return f"Deleted '{target.name}'."

    except Exception as e:

        return f"Error deleting: {e}"


# =====================================================
# Open Recycle Bin
# =====================================================

def open_recycle_bin():

    try:

        subprocess.Popen(
            [
                "explorer.exe",
                "shell:RecycleBinFolder"
            ]
        )

        return "Opening Recycle Bin."

    except Exception as e:

        return f"Error opening Recycle Bin: {e}"