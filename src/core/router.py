import re


def route(command):

    command = command.lower().strip()

    # -----------------------------
    # Normalize speech variations
    # -----------------------------

    command = re.sub(
        r"person\s+(one|won|on)",
        "person 1",
        command
    )

    command = re.sub(
        r"mark\s+(one|won|on)",
        "mark 1",
        command
    )

    # =====================================================
    # Exit
    # =====================================================

    if command in [
        "exit",
        "quit",
        "goodbye",
        "stop"
    ]:
        return {
            "action": "exit"
        }

    # =====================================================
    # Time
    # =====================================================

    if "time" in command:
        return {
            "action": "time"
        }

    # =====================================================
    # Dictation
    # =====================================================

    if command in [
        "dictation",
        "start dictation",
        "dictate",
        "start writing"
    ]:
        return {
            "action": "dictation"
        }

    # =====================================================
    # Remember
    # =====================================================

    match = re.search(
        r"remember my (.+?) is (.+)",
        command
    )

    if match:
        return {
            "action": "remember",
            "key": match.group(1).strip(),
            "value": match.group(2).strip()
        }

    # =====================================================
    # Recall
    # =====================================================

    match = re.search(
        r"(what is|what's|whats) my (.+)",
        command
    )

    if match:
        return {
            "action": "recall",
            "key": match.group(2).strip()
        }

    # =====================================================
    # Forget
    # =====================================================

    match = re.search(
        r"forget my (.+)",
        command
    )

    if match:
        return {
            "action": "forget",
            "key": match.group(1).strip()
        }

    # =====================================================
    # Chrome Profile - Direct Open
    # =====================================================

    match = re.match(
        r"open (mark 1|person 1) chrome$",
        command
    )

    if match:
        return {
            "action": "profile_open",
            "profile": match.group(1)
        }

    # =====================================================
    # Chrome - Choose Profile
    # =====================================================

    if command in [
        "open chrome",
        "open google chrome",
        "launch chrome",
        "launch google chrome"
    ]:
        return {
            "action": "chrome_choose_profile"
        }

    # =====================================================
    # Google Search In Profile
    # =====================================================

    match = re.match(
        r"search google for (.+) in (mark 1|person 1)",
        command
    )

    if match:
        return {
            "action": "profile_google_search",
            "target": match.group(1).strip(),
            "profile": match.group(2).strip()
        }

    # =====================================================
    # YouTube Search In Profile
    # =====================================================

    match = re.match(
        r"search youtube for (.+) in (mark 1|person 1)",
        command
    )

    if match:
        return {
            "action": "profile_youtube_search",
            "target": match.group(1).strip(),
            "profile": match.group(2).strip()
        }

    # =====================================================
    # Open Website In Profile
    # =====================================================

    match = re.match(
        r"open (.+?) in (mark 1|person 1)(?: chrome)?$",
        command
    )

    if match:
        return {
            "action": "profile_website",
            "target": match.group(1).strip(),
            "profile": match.group(2).strip()
        }

    # =====================================================
    # Google Search
    # =====================================================

    if command.startswith("search google for"):

        return {
            "action": "google_search",
            "target": command.replace(
                "search google for",
                "",
                1
            ).strip()
        }

    # =====================================================
    # YouTube Search
    # =====================================================

    if command.startswith("search youtube for"):

        return {
            "action": "youtube_search",
            "target": command.replace(
                "search youtube for",
                "",
                1
            ).strip()
        }

    # =====================================================
    # Open Recycle Bin
    # =====================================================

    if command in [
        "open recycle bin",
        "open recyclebin",
        "open trash",
        "open bin"
    ]:
        return {
            "action": "open_recycle_bin"
        }

    # =====================================================
    # Open Known Folder
    # =====================================================

    # IMPORTANT:
    # Do NOT use .+ here.
    #
    # Otherwise:
    # open chrome
    # open notepad
    #
    # would become open_folder.

    match = re.match(
        r"open (desktop|documents|downloads|pictures|music|videos)$",
        command
    )

    if match:

        return {
            "action": "open_folder",
            "target": match.group(1).strip()
        }

    # =====================================================
    # Create Folder
    # =====================================================

    match = re.match(
        r"(?:create|make)\s+(?:a\s+)?folder"
        r"(?:\s+(?:called|named|name))?\s+(.+)",
        command
    )

    if match:

        return {
            "action": "create_folder",
            "target": match.group(1).strip()
        }

    # =====================================================
    # Create File
    # =====================================================

    match = re.match(
        r"(?:create|make)\s+(?:a\s+)?file"
        r"(?:\s+(?:called|named|name))?\s+(.+)",
        command
    )

    if match:

        return {
            "action": "create_file",
            "target": match.group(1).strip()
        }

    # =====================================================
    # Rename
    # =====================================================

    match = re.match(
        r"rename (?:file|folder)?\s*(.+?)\s+to\s+(.+)",
        command
    )

    if match:

        return {
            "action": "rename",
            "old_name": match.group(1).strip(),
            "new_name": match.group(2).strip()
        }

    # =====================================================
    # Delete Folder
    # =====================================================

    match = re.match(
        r"(?:delete|remove)\s+"
        r"(?:the\s+)?"
        r"(?:a\s+)?"
        r"folder\s+"
        r"(?:(?:called|named|name)\s+)?"
        r"(.+)",
        command
    )

    if match:

        return {
            "action": "delete_folder",
            "target": match.group(1).strip()
        }

    # =====================================================
    # Delete File
    # =====================================================

    match = re.match(
        r"(?:delete|remove)\s+"
        r"(?:the\s+)?"
        r"(?:a\s+)?"
        r"file\s+"
        r"(?:(?:called|named|name)\s+)?"
        r"(.+)",
        command
    )

    if match:

        return {
            "action": "delete_file",
            "target": match.group(1).strip()
        }

    # =====================================================
    # Open Website / Application
    # =====================================================

    if command.startswith("open "):

        item = command.replace(
            "open ",
            "",
            1
        ).strip()

        websites = [
            "google",
            "youtube",
            "github",
            "gmail",
            "chatgpt",
            "chat gpt",
            "instagram",
            "facebook",
            "linkedin",
            "twitter",
            "x",
            "amazon",
            "netflix",
            "whatsapp",
            "spotify",
            "reddit",
            "stackoverflow"
        ]

        if item in websites:

            return {
                "action": "open_website",
                "target": item
            }

        # Anything else after "open"
        # is treated as an application.

        return {
            "action": "open_app",
            "target": item
        }

    # =====================================================
    # AI Chat
    # =====================================================

    return {
        "action": "chat",
        "target": command
    }