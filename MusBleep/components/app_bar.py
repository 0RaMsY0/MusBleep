import pynecone as pc

from .musBleep_logo import musBleepLogo
from MusBleep.state import MusBleepState
from MusBleep.vars import GITHUB_REPO

def appBar():
    """
        App bar for the web app
    """
    return pc.box(
        pc.hstack(
                pc.link(
                    pc.hstack(
                        musBleepLogo(),
                        pc.text(
                            "MusBleep",
                            background_image="linear-gradient(271.68deg, #0000FF 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            font_weight=600,
                            font_size="1.5em",
                        ),
                        spacing="0.5em"
                    ),
                    href="/",
                    _hover={"text_decoration": "none"},    
                ),
                pc.hstack(
                    pc.button(
                        pc.cond(
                            MusBleepState.is_darkMode != True,
                            pc.image(
                                src="/dark-mode.png",
                                height="2em"
                            ),
                            pc.image(
                                src="/light-mode.png",
                                height="2em",
                            ),
                        ),
                        on_click=MusBleepState.change_mode(),
                        bg="#FFFFFF",
                    ),
                    pc.spacer(
                        width="0.3em",
                    ),
                    pc.link(
                        pc.image(
                            src="/github.png",
                            height="2em"
                        ),
                        href=GITHUB_REPO
                    ),
                ),
                justify="space-between",
                padding_x="2em",
            ),
        padding_y=["4em", "5em", "1em"],
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )
