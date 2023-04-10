import pynecone as pc

from MusBleep.state import MusBleepState

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
                is_disabled=not MusBleepState.is_upload_finish
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
                is_disabled=not MusBleepState.is_upload_finish
            )
        ),
        width="20m",
        background_repeat="no-repeat",
        background_size="15em",
        background_position="135% 150%",
        margin_bottom="1em",
        style= {
            "background": "blue",
            "border": "1px solid #b9f0ef",
            "border_radius": "5em",
            "padding": "1em",
            "box_shadow": """
                rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
                """,
            "height": "100%",
            "align_items": "left",
            "width": "100%",
            "min_height": "5em",
            "padding": "2em",
            "bg": "rgba(248, 248, 248, .75)",
            "_hover": {
                "box_shadow": """
                rgba(23, 6, 100, 0.035) 0px 24px 22px 0px, rgba(23, 6, 100, 0.055) 0px 8.5846px 8.03036px 0px, rgba(23, 6, 100, 0.067) 0px 4.77692px 3.89859px 0px, rgba(23, 6, 100, 0.082) 0px 2.63479px 1.91116px 0px, rgba(23, 6, 100, 0.12) 0px 1.15891px 0.755676px 0px
            """,
            },
        }
    )
