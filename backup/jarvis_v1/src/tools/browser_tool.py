from services.browser import (
    open_website,
    search_google,
    search_youtube
)


class BrowserTool:

    def execute(self, action, data):

        if action == "open_website":
            return open_website(data["target"])

        elif action == "google_search":
            return search_google(data["target"])

        elif action == "youtube_search":
            return search_youtube(data["target"])

        return None