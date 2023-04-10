import pynecone as pc

def title():
    """
        Returns a title that says
        `MusBleep: Silence the explicit lyrics`
    """
    return pc.vstack(
        pc.hstack(
            pc.text(
                "MusBleep",
                background_image="linear-gradient(271.68deg, #0000FF 0.75%, #756AEE 88.52%)",
                background_clip="text",
                font_weight="bold",
                font_size="4em",
            ),
            pc.text(
                ": Silence",
                font_weight="bold",
                font_size="4em",
            ),
        ),
        pc.text(
                "the explicit lyrics",
                font_weight="bold",
                font_size="4em",
            )
    )
