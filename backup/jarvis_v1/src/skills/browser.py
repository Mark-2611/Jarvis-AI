import subprocess
import urllib.parse
import webbrowser

from config.browser_profiles import CHROME_PATH, CHROME_PROFILES


WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "instagram": "https://instagram.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
    "amazon": "https://amazon.in",
    "netflix": "https://netflix.com",
    "whatsapp": "https://web.whatsapp.com",
}


def open_website(site):

    site = site.lower()

    if site in WEBSITES:
        webbrowser.open(WEBSITES[site])
    else:
        webbrowser.open(f"https://{site}.com")


def search_google(query):

    webbrowser.open(
        "https://www.google.com/search?q="
        + urllib.parse.quote(query)
    )


# --------------------------------------------------
# Chrome Profile
# --------------------------------------------------

def open_chrome_profile(profile):

    profile = profile.lower()

    if profile not in CHROME_PROFILES:
        return f"I don't know the Chrome profile {profile}."

    subprocess.Popen([
        CHROME_PATH,
        f"--profile-directory={CHROME_PROFILES[profile]}"
    ])

    return f"Opening {profile} Chrome."


def open_website_in_profile(profile, website):

    profile = profile.lower()

    if profile not in CHROME_PROFILES:
        return f"I don't know the Chrome profile {profile}."

    url = WEBSITES.get(
        website.lower(),
        f"https://{website}.com"
    )

    subprocess.Popen([
        CHROME_PATH,
        f"--profile-directory={CHROME_PROFILES[profile]}",
        url
    ])

    return f"Opening {website} in {profile}."


def google_search_in_profile(profile, query):

    profile = profile.lower()

    if profile not in CHROME_PROFILES:
        return f"I don't know the Chrome profile {profile}."

    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(query)
    )

    subprocess.Popen([
        CHROME_PATH,
        f"--profile-directory={CHROME_PROFILES[profile]}",
        url
    ])

    return f"Searching {query} in {profile}."