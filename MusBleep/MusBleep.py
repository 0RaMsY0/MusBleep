import pynecone as pc
from pcconfig import config

from .components.app_bar import appBar
from .components.title import title
from .components.play_music import playMusic
from .components.drag_or_drop_upload import dragOrDropUpload
from .vars import STYLESHEETS
from .vars import ERROR_MESSAGES, SUCCESS_MESSAGES, MESSAGES_STATUS
from .state import MusBleepState

def index() -> pc.Component:
    return pc.vstack(
        appBar(),
        pc.center(
            title(),
        ),
        pc.spacer(
            height="7em"
        ),
        playMusic(),
        pc.spacer(
            height="4em"
        ),
        pc.cond(
            MusBleepState.show_ending_message,
            pc.box(
                pc.tablet_and_desktop(
                    pc.box(
                        pc.alert(
                            pc.alert_icon(),
                            pc.alert_title(
                                MusBleepState.ending_message,
                            ),
                            status=MusBleepState.message_status,
                        ),
                        width="17em"
                    ),
                ),
                pc.mobile_only(
                    pc.box(
                        pc.alert(
                            pc.alert_icon(),
                            pc.alert_title(
                                MusBleepState.ending_message,
                            ),
                            status=MusBleepState.message_status,
                        ),
                        width="12em"
                    ),
                ),
            ),
            pc.cond(MusBleepState.is_upload_started,
                pc.CircularProgress(
                    color="black",
                    is_indeterminate=True
                ),
                dragOrDropUpload(),
            ),
        ),
    )

# Add state and page to the app.
app = pc.App(
    state=MusBleepState,
    stylesheets=STYLESHEETS
)
app.add_page(index, title="MusBleep")
app.compile()
