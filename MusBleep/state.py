import requests
import pynecone as pc

from MusBleep.vars import ERROR_MESSAGES, SUCCESS_MESSAGES, MESSAGES_STATUS

class MusBleepState(pc.State):
    """
        Main state handler for the web app
    """
    is_darkMode = True

    def change_mode(self):
        """
            Changes the mode
        """
        self.is_darkMode = not self.is_darkMode

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

        API_URL = "http://127.0.0.1:9090"

        MUSIC_CONTENT = await file.read()
        MUSIC_NAME = file.filename

        self.music_name = MUSIC_NAME

        print(MUSIC_NAME)
        FILE = {
            "file": MUSIC_CONTENT
        }
        PARAMS = {
            "music_name": MUSIC_NAME
        }

        RESPONCE = requests.post(
            f"{API_URL}/api/v1/bleep_music",
            files=FILE,
            params=PARAMS
        )
        
        if RESPONCE.status_code == 400:
            self.is_music_upload_exception_raised = True
            self.ending_message = ERROR_MESSAGES[0]
        
        elif RESPONCE.status_code == 409:
            self.is_faild_to_bleep_music_exception_raised = True
            self.ending_message = ERROR_MESSAGES[1]
        
        elif RESPONCE.status_code == 201:
            self.bleeped_music_url = f"{API_URL}{RESPONCE.json()['bleeped_music_path']}"
            self.ending_message = SUCCESS_MESSAGES[0]

        print(f"{RESPONCE.json() = }")

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