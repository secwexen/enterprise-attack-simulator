import platform


def get_platform():
    system = platform.system().lower()
    if system.startswith("win"):
        return "windows"
    if system.startswith("linux"):
        return "linux"
    if system.startswith("darwin"):
        return "macos"
    return "unknown"
