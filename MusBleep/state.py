import requests
import pynecone as pc

from MusBleep.vars import ERROR_MESSAGES, SUCCESS_MESSAGES, MESSAGES_STATUS
from MusBleep.utils.check_api import check_api
from MusBleep.utils.read_conf import conf

class MusBleepState(pc.State):
    """
        Main state handler for the web app
    """
    # Loading animation
    is_upload_started: bool = False

    # Ending message
    show_ending_message: bool = False
    ending_message: str = ""
    message_status: str = ""

    # Music Upload
    bleeped_music_url: str = ""
    music_name: str = "Nothing to show"  # default value
    is_upload_finish: bool = False
    is_music_upload_exception_raised: bool = False # Used to show a warning when the music upload fails
    is_faild_to_bleep_music_exception_raised: bool = False

    # Play Music states
    is_playing: bool = False

    async def handle_music_upload(self, file: pc.UploadFile):
        """
            Upload the music to the API 
            to get bleeped
        """
        self.is_upload_started = True

        if check_api() != True:
            self.show_ending_message = True
            self.ending_message = "Faild to connect to the api, please make sure it is running"
            self.message_status = MESSAGES_STATUS[self.ending_message]
            self.is_upload_finish = True
            self.is_upload_started = False

            return

        API_URL = conf()["api"]
        MUSIC_NAME = file.filename if ' ' not in file.filename else file.filename.replace(' ', '_')
        SAVE_MUSIC_PATH = f"MusBleep/api/cache/{MUSIC_NAME}"
        
        try:
           with open(SAVE_MUSIC_PATH, "wb") as save_music:
               while music_content := file.file.read(1024 * 1024):
                   save_music.write(music_content)
        except Exception as exception:
            self.is_music_upload_exception_raised = True
            self.ending_message = ERROR_MESSAGES[0]
            self.is_upload_finish  = True
            self.show_ending_message = True
            self.is_upload_started = False
            self.message_status = MESSAGES_STATUS[self.ending_message]
            return
        finally:
            file.file.close()
        
        self.music_name = MUSIC_NAME if len(MUSIC_NAME) < 17 else f"{MUSIC_NAME[:17]} ..."

        PARAMS = {
            "music_name": f"cache/{MUSIC_NAME}"
        }

        RESPONCE = requests.get(
            f"{API_URL}/api/v1/bleep_music",
            params=PARAMS
        )

        if RESPONCE.status_code == 409:
            self.is_faild_to_bleep_music_exception_raised = True
            self.ending_message = ERROR_MESSAGES[1]
        
        elif RESPONCE.status_code == 200:
            self.bleeped_music_url = f"{API_URL}{RESPONCE.json()['bleeped_music_path']}"
            self.ending_message = SUCCESS_MESSAGES[0]

        self.is_upload_finish  = True
        self.show_ending_message = True
        self.is_upload_started = False

        self.message_status = MESSAGES_STATUS[self.ending_message]

    def update_upload_exception_state(self):
        """
            Updates the `is_music_upload_exception_raised` value
        """
        self.is_music_upload_exception_raised = not self.is_music_upload_exception_raised

    def update_faild_to_bleep_music_exception_state(self):
        """
            Updates the `is_faild_to_bleep_music_exception_raised` value
        """
        self.is_faild_to_bleep_music_exception_raised = not self.is_faild_to_bleep_music_exception_raised

    def update_playing_state(self):
        """
            Updates the `is_playing` value
        """
        self.is_playing = not self.is_playing

    def redirect_to_download_music(self):
        """
            Redirects to the download music music
            in order to install it
        """
        return pc.redirect(MusBleepState.bleeped_music_url)
