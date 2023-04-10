import pynecone as pc

from MusBleep.state import MusBleepState

def faildToUploadMusic() -> pc.Component:
    """
        Shows an alert dialogue when an error
        happens while upload the file to the API
    """
    return pc.alert_dialog(
        pc.alert_dialog_overlay(
            pc.alert_dialog_content(
                pc.alert_dialog_header("Warning"),
                pc.alert_dialog_body(
                    "Faild to upload the music to the API, please try again"
                ),
                pc.alert_dialog_footer(
                    pc.button(
                        "Ok",
                        on_click=MusBleepState.update_upload_exception_state(),
                    )
                ),
            )
        ),
        is_open=MusBleepState().is_music_upload_exception_raised,
    )

def faildToBleepMusic() -> pc.Component:
    """
        Shows an alert dialogue when an error
        happens while upload the file to the API
    """
    return pc.alert_dialog(
        pc.alert_dialog_overlay(
            pc.alert_dialog_content(
                pc.alert_dialog_header("Warning"),
                pc.alert_dialog_body(
                    "Faild to bleep the music, please try again later"
                ),
                pc.alert_dialog_footer(
                    pc.button(
                        "Ok",
                        on_click=MusBleepState.update_faild_to_bleep_music_exception_state(),
                    )
                ),
            )
        ),
        is_open=MusBleepState.is_faild_to_bleep_music_exception_raised,
    )
