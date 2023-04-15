import os
import json

def conf() -> dict:
    """
        This function reads a JSON configuration
        file located at `CONF_FILE_PATH` and returns
        its contents as a Python dictionary
    """
    CONF_FILE_PATH = "MusBleep/conf/MusBleep-conf.json"
    CONF_FILE_CONTENT = json.loads(open(CONF_FILE_PATH, "r").read())

    return CONF_FILE_CONTENT
