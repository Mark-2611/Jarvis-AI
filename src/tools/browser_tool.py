from services.browser import (
    open_website,
    search_google,
    search_youtube,
    open_chrome_profile,
    open_website_in_profile,
    google_search_in_profile,
    youtube_search_in_profile
)


class BrowserTool:

    def execute(self, action, data):

        if action == "open_website":
            return open_website(data["target"])

        elif action == "google_search":
            return search_google(data["target"])

        elif action == "youtube_search":
            return search_youtube(data["target"])

        elif action == "profile_open":
            return open_chrome_profile(data["profile"])

        elif action == "profile_website":
            return open_website_in_profile(
                data["profile"],
                data["target"]
            )

        elif action == "profile_google_search":
            return google_search_in_profile(
                data["profile"],
                data["target"]
            )

        elif action == "profile_youtube_search":
            return youtube_search_in_profile(
                data["profile"],
                data["target"]
            )

        return None