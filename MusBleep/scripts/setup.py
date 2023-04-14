import os
import sys
import platform
import subprocess

try:
    import typer
except:
    subprocess.run(
        "pip install typer[all]",
        shell=True,
        capture_output=True,
    )

try:
    import rich
except:
    subprocess.run(
        "pip install rich",
        shell=True,
        capture_output=True,
    )

import typer
from rich import print

# Init CLI
CLI = typer.Typer()

def install_python_libs() -> None:
    """
        Installes the needed python packages
    """
    PYTHON_PACKAGES = [
       "fastapi",
       "uvicorn",
       "pynecone",
       "git+https://github.com/linto-ai/whisper-timestamped"
    ]

    for package in PYTHON_PACKAGES:
        COMMAND = f"pip install -U {package}"

        print(f"\n[green] ==> [white]Downloading [yellow]`{package}`[white]")
        print(f"\t[green]↳ [cyan]{COMMAND}[white]")

        subprocess.run(
            COMMAND,
            shell=True,
        )

def install_bun() -> None:
    """
        Download the bun package
    """
    COMMAND = "curl -fsSL https://bun.sh/install | bash"

    print(f"\t[green]↳ [cyan]{COMMAND}[white]")

    subprocess.run(
        COMMAND,
        shell=True
    )

def install_node() -> None:
    """
        Installs node.js for only linux
        based OS, for Windows users please 
        visit https://nodejs.org/en to 
        install it.
    """
    NODESOURCE = "https://deb.nodesource.com/setup_19.x"
    COMMAND = f"curl -fsSL {NODESOURCE} | sudo bash -"

    print(f"\t[green]↳ [cyan]{COMMAND}white")

    subprocess.run(
        COMMAND, 
        shell=True,
    )

@CLI.command()
def setup() -> None:
    """
        Setup MusBleep
    """
    print("\n[green] [  +  ] [white] Installing [blue]`Python Libs`[white]")
    install_python_libs()

    print("\n[green] [  +  ] [white] Installing [blue]`bun`[white]")
    install_bun()

    if platform.system() == "Windows":
        print("\n[red] [  -  ] [white] Please visit [yellow]`https://nodejs.org/en` [white]to download [yellow]`NodeJS`")
        sys.exit(1)
    
    install_node()

def run() -> None:
    """
        Runs the CLI
    """
    PYTHON_VERSION = subprocess.run(
        "python --version",
        shell=True,
        capture_output=True
    ).stdout.strip().decode().replace("Python ", "").split(".")[0:2]

    if float(".".join(PYTHON_VERSION)) < 3.10:
        print("\n[red] [  -  ] [white] Unsupported [blue]`python version`[white] please upgrade to [cyan]`3.10` [white] or higher")
        sys.exit(1)

    CLI()

if __name__ == "__main__":
    run()
