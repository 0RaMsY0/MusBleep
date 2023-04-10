import pynecone as pc

def musBleepLogo():
    """
        Returns a pc.image object of the
        MusBleep logo
    """
    return pc.image(
        src="/MusBleep.png",
        height="2.5em"
    )
