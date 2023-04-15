import pynecone as pc

from MusBleep.state import MusBleepState

def dragOrDropUpload():
    """
        Drag or drop to upload form
    """
    return pc.vstack(
        pc.tablet_and_desktop(
            pc.upload(
                pc.vstack(
                    pc.button(
                        "Select File",
                        color="rgb(107,99,246)",
                        bg="white",
                        border=f"1px solid rgb(107,99,246)",
                    ),
                    pc.text(
                        "Drag and drop music file here or click to select a music file"
                        
                    ),
                ),
                    border="1px dotted rgb(107,99,246)",
                    padding="5em",
                ),
            ),
            pc.mobile_only(
                pc.upload(
                    pc.vstack(
                        pc.button(
                            "Select File",
                            color="rgb(107,99,246)",
                            bg="white",
                            border=f"1px solid rgb(107,99,246)",
                        ),
                        pc.text(
                            "Drag and drop music file here or click to select a music file"
                            
                        ),
                    ),
                        border="1px dotted rgb(107,99,246)",
                        padding="2em",
                width="14em",
                ),
            ),
            pc.button(
                "Upload",
                on_click=lambda: MusBleepState.handle_music_upload(
                    pc.upload_files()
                ),
            ),
        )
