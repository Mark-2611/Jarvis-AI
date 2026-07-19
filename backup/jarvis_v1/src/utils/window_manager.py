import time
import pygetwindow as gw

_last_window_title = None


def set_last_window(title):
    global _last_window_title
    _last_window_title = title


def get_last_window():
    return _last_window_title


def focus_last_window():

    if not _last_window_title:
        return False

    windows = gw.getWindowsWithTitle(_last_window_title)

    if not windows:
        return False

    window = windows[0]

    if window.isMinimized:
        window.restore()

    window.activate()

    time.sleep(0.5)

    return True