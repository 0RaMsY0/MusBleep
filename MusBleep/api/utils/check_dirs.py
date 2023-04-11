import os

def check_dirs() -> None:
    """
        Checks for the needed dirs [`cache`, `output`]
        that doesn't come precreated due to .gitignore
    """
    DIRS = ["cache", "output"]

    for dir in DIRS:
        if dir not in os.listdir("."):
            os.mkdir(f"./{dir}")
        continue
