import subprocess
import whisper_timestamped as whisper

from loguru import logger

from utils.printl import printl
from utils.curse_words import curse_words

async def bleep_vocals(music_path: str, output_path: str | None = "output") -> str:
    """
        Takes in the vocals path then uses
        whisper to extract lyrics/text from
        the vocals then try to find the 
        explicit words to bleep.
    """
    AUDIO = whisper.load_audio(music_path)
    MODEL = whisper.load_model("small", device="cpu")
    RESULT = whisper.transcribe(MODEL, AUDIO, language="en")
    
    MUSIC_OUTPUT_PATH = f"output/{music_path.split('/')[-1]}" if output_path == "output" else f"{output_path}/{music_path.split('/')[-1]}"

    # [NOTE]: This swear words were writen in the purpos of detecting them
    # in the vocals and bleeping them.
    SWEAR_WORDS = curse_words()

    BASE_FILTERS = []
    BLEEP_FILTERS = []

    PREVIOUS_FILTER_END = 0

    for segment in RESULT["segments"]:
        for word in segment["words"]:
            word_text = word["text"].lower().strip('.!?{}[]()+=_-@#$%^&*~`"|/')
            for swear_word in SWEAR_WORDS:
                if swear_word in word_text:
                    start = word["start"]
                    end = word["end"]

                    BASE_FILTERS.append(
                        f"volume=enable='between(t,{start},{end})':volume=0"
                    )
                    BLEEP_FILTERS.append(
                        f"volume=enable='between(t,{PREVIOUS_FILTER_END},{start})':volume=0"
                    )
                    PREVIOUS_FILTER_END = end

    # Arbitrary value for a year in seconds
    LENGTH = 365 * 24 * 60 * 60
    
    BLEEP_FILTERS.append(
        f"volume=enable='between(t,{PREVIOUS_FILTER_END},{LENGTH})':volume=0"
    )

    FFMPEG_COMMAND = f"ffmpeg -hide_banner -i \"{music_path}\" -f lavfi -i \"sine=frequency=1000\" -filter_complex \"[0:a]volume=1,{','.join(BASE_FILTERS)}[0x];[1:a]volume=1,{','.join(BLEEP_FILTERS)}[1x];[0x][1x]amix=inputs=2:duration=first\" -c:a libmp3lame -q:a 4 -y \"{MUSIC_OUTPUT_PATH}\""
    CLEAN_UP = f"rm \"{music_path}\""
    
    logger.info(f"ffmpeg command: {FFMPEG_COMMAND}")

    subprocess.run(
        FFMPEG_COMMAND,
        shell=True,
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL
    )
    subprocess.run(
        CLEAN_UP,
        shell=True,
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL
    )
    
    return MUSIC_OUTPUT_PATH
