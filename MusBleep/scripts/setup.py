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
    )

try:
    import rich
except:
    subprocess.run(
        "pip install rich",
        shell=True,
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
       "rich",
       "git+https://github.com/linto-ai/whisper-timestamped"
    ]

    for package in PYTHON_PACKAGES:
        COMMAND = f"pip install -U {package}"

        print(f"[green] ==> [white]Downloading [yellow]`{package}`[white]")
        print(f"\t[green]↳ [cyan]{COMMAND}[white]")

        subprocess.run(
            COMMAND,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )

def install_bun() -> None:
    """
        Download the bun package
    """
    COMMAND = "curl -fsSL https://bun.sh/install | bash"

    print(f"\t[green]↳ [cyan]{COMMAND}[white]")

    subprocess.run(
        COMMAND,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
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

    print(f"\t[green]↳ [cyan]{COMMAND}[white]")

    subprocess.run(
        COMMAND, 
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )

def install_ffmpeg() -> None:
    """
        Installs ffmpeg
    """
    COMMAND = "git clone https://git.ffmpeg.org/ffmpeg.git ~/ffmpeg"
    CONFIGURE_FFMPEG_COMMAND = "cd ~/ffmpeg && ./configure"
    INSTALL_FFMPEG = "cd ~/ffmpeg && make && make install"

    print(f"\t[green]↳ [cyan]{COMMAND}[white]")
    subprocess.run(
        COMMAND,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )

    print(f"\t[green]↳ [cyan]{CONFIGURE_FFMPEG_COMMAND}[white]")
    subprocess.run(
        CONFIGURE_FFMPEG_COMMAND,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )

    print(f"\t[green]↳ [cyan]{INSTALL_FFMPEG}[white]")
    subprocess.run(
        INSTALL_FFMPEG,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )

@CLI.command()
def setup() -> None:
    """
        Setup MusBleep
    """
    print("[green] [  +  ] [white] Installing [blue]`Python Libs`[white]")
    install_python_libs()

    print("[green] [  +  ] [white] Installing [blue]`bun`[white]")
    install_bun()

    if platform.system() == "Windows":
        print("[red] [  -  ] [white] Please visit [yellow]`https://nodejs.org/en` [white]to download [yellow]`NodeJS`")
        sys.exit(1)
    
    print("[green] [  +  ] [white] Installing [blue]`node`[white]")
    install_node()

    print("[green] [  +  ] [white] Installing [blue]`ffmpeg`[white]")
    install_ffmpeg()

def run() -> None:
    """
        Runs the CLI
    """
    PYTHON_VERSION = subprocess.run(
        "python3 --version",
        shell=True,
        capture_output=True
    ).stdout.strip().decode().replace("Python ", "").split(".")[0:2]

    if float(".".join(PYTHON_VERSION)) < 3.10:
        print("[red] [  -  ] [white] Unsupported [blue]`python version`[white] please upgrade to [cyan]`3.10` [white] or higher")
        sys.exit(1)

    CLI()

if __name__ == "__main__":
    run()
