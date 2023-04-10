import colorama

def printl(text: str, end: bool | None = False) -> None:
    """
        Takes in text then print it
        out to the console with colors
    """
    COLORS = {
        "red": colorama.Fore.RED,
        "blue": colorama.Fore.BLUE,
        "cyan": colorama.Fore.CYAN,
        "yellow": colorama.Fore.YELLOW,
        "reset": colorama.Fore.RESET,
        "green": colorama.Fore.GREEN,
        "white": colorama.Fore.WHITE,
        "reset": colorama.Fore.RESET
    }
    _text = text

    for color in COLORS:
        if f"[{color}]" in _text:
            _text = _text.replace(f"[{color}]", COLORS[color])
                 
    print(_text, end="" if end else "")

