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

        # =================================================
        # Open Website
        # =================================================

        if action == "open_website":

            return open_website(
                data["target"]
            )

        # =================================================
        # Google Search
        # =================================================

        elif action == "google_search":

            return search_google(
                data["target"]
            )

        # =================================================
        # YouTube Search
        # =================================================

        elif action == "youtube_search":

            return search_youtube(
                data["target"]
            )

        # =================================================
        # Open Specific Chrome Profile
        # =================================================

        elif action == "profile_open":

            return open_chrome_profile(
                data["profile"]
            )

        # =================================================
        # Choose Chrome Profile
        # =================================================

        elif action == "chrome_choose_profile":

            return {
                "status": "choose_chrome_profile"
            }

        # =================================================
        # Open Website In Chrome Profile
        # =================================================

        elif action == "profile_website":

            return open_website_in_profile(
                data["profile"],
                data["target"]
            )

        # =================================================
        # Google Search In Chrome Profile
        # =================================================

        elif action == "profile_google_search":

            return google_search_in_profile(
                data["profile"],
                data["target"]
            )

        # =================================================
        # YouTube Search In Chrome Profile
        # =================================================

        elif action == "profile_youtube_search":

            return youtube_search_in_profile(
                data["profile"],
                data["target"]
            )

        return None