import webbrowser
from urllib.parse import quote

# -----------------------------
# Website URLs
# -----------------------------
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chatgpt.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "spotify": "https://open.spotify.com",
    "amazon": "https://www.amazon.in",
    "netflix": "https://www.netflix.com",
}


# -----------------------------
# Open any supported website
# -----------------------------
def open_website(site):

    site = site.lower().strip()

    # Speech aliases
    aliases = {
        "chat gpt": "chatgpt",
        "git hub": "github",
        "linked in": "linkedin",
        "you tube": "youtube",
        "face book": "facebook",
    }

    site = aliases.get(site, site)

    if site in WEBSITES:
        webbrowser.open(WEBSITES[site])
        return f"Opening {site}."

    return f"I don't know how to open {site}."


# -----------------------------
# Individual website functions
# -----------------------------
def open_google():
    return open_website("google")


def open_youtube():
    return open_website("youtube")


def open_github():
    return open_website("github")


def open_gmail():
    return open_website("gmail")


def open_chatgpt():
    return open_website("chatgpt")


def open_instagram():
    return open_website("instagram")


def open_facebook():
    return open_website("facebook")


def open_linkedin():
    return open_website("linkedin")


def open_spotify():
    return open_website("spotify")


def open_amazon():
    return open_website("amazon")


def open_netflix():
    return open_website("netflix")


# -----------------------------
# Google Search
# -----------------------------
def search_google(query):

    url = f"https://www.google.com/search?q={quote(query)}"
    webbrowser.open(url)

    return f"Searching Google for {query}."


# -----------------------------
# YouTube Search
# -----------------------------
def search_youtube(query):

    url = f"https://www.youtube.com/results?search_query={quote(query)}"
    webbrowser.open(url)

    return f"Searching YouTube for {query}."