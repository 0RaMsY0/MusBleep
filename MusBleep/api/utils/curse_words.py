import json
import base64
from loguru import logger

from .read_conf import conf

def curse_words() -> list[str]:
    """
        Decodes the curse words located
        at `conf/api-conf.json` and returns 
        them in form of list of strings
    """
    CURSE_WORDS = conf()["curse_words"]
    DECODED_CURSE_WORDS = []

    for word in CURSE_WORDS:
        if is_base64(word):
            DECODED_CURSE_WORDS.append(base64.b64decode(word).decode())
        else:
            logger.critical(f"\"{word}\" is not encoded in base64")

    return DECODED_CURSE_WORDS

def is_base64(SB) -> bool:
    """
        Checks if the given `SB` is encoded
        in bas64 or not

        * output:
            returns a boolean 
    """
    try:
        if isinstance(SB, str):
                # If there's any unicode here, an exception will be thrown and the function will return false
                SB_BYTES = bytes(SB, 'ascii')
        elif isinstance(sb, bytes):
                SB_BYTES = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(SB_BYTES)) == SB_BYTES
    except Exception:
            return False
