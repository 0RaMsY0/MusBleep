import pynecone as pc

from MusBleep.state import MusBleepState
from MusBleep.vars import PLAY_MUSIC_CARD_STYLE

def playMusic() -> pc.Component:
    """
        Returns a music player to play
        the bleeped version of the uploaded
        music
    """
    return pc.box(
        pc.hstack(
            pc.button(
                pc.image(
                     src="/play-button.png",
                     height="2.5em"
                ),
                height="4em",
                bg="#FFFFFF",
                is_disabled= True if MusBleepState.is_upload_finish == False else False
            ),
            pc.cond(
                MusBleepState.music_name != "Nothing to show",
                pc.text(
                    MusBleepState.music_name,
                    font_weight=600,
                    font_size="1.5em",
                ),
                pc.text(
                    MusBleepState.music_name,
                    font_weight=500,
                    as_="i",
                    font_size="1.5em",
                ), 
            ),
            pc.spacer(
                width="5em"
            ),
            pc.button(
                pc.image(
                    src="/download.png",
                    height="2.9em",
                ),
                height="4em",
                bg="#FFFFFF",
                is_disabled=True if MusBleepState.is_upload_finish == False else False,
                on_click=MusBleepState.redirect_to_download_music()
            )
        ),
        width="20m",
        background_repeat="no-repeat",
        background_size="15em",
        background_position="135% 150%",
        margin_bottom="1em",
        style=PLAY_MUSIC_CARD_STYLE,
    )

