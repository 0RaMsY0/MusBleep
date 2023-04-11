import subprocess
import whisper_timestamped as whisper

from utils.printl import printl

def bleep_vocals(music_path: str, output_path: str | None = "output") -> str:
    """
    Takes in the vocals path then uses
    whisper to extract lyrics/text from
    the vocals then try to find the 
    explicit words to bleep.
    """
    AUDIO = whisper.load_audio(music_path)
    MODEL = whisper.load_model("small", device="cpu")
    RESULT = whisper.transcribe(MODEL, AUDIO, language="en")
    
    MUSIC_OUTPUT_PATH = f"output/{music_path.split('/')[-1]}"

    # [NOTE]: This swear words were writen in the purpos of detecting them
    # in the vocals and bleeping them.
    SWEAR_WORDS = [
        "fuck",             "bitch",            "bitches"           "shit",
        "damn",             "ass",              "pussy",            "nigga",
        "whore",            "dick",             "cock",             "arse",
        "arsehead",         "arsehole",         "ass",              "asshole",
        "bastard",          "bloody",           "bollocks"          "brotherfucker",
        "bugger",           "bullshit",         "cocksucker",       "crap",
        "cunt",             "damn it",          "dickhead",         "dyke",
        "fatherfucker",     "frigger",          "goddamn",          "godsdamn",
        "hell",             "holy shit",        "horseshit",        "kike",
        "motherfucker",     "nigra",            "piss",             "prick",
        "shite",            "sisterfucker",     "slut",             "spastic",
        "turd",             "fucking",          "hoe",              "f***ing"
        "porn",             "pornhub",          "boobs",            "breasts",
        "breast",           "tiddies",          "tiddy",            "striper"
    ]
    
    BASE_FILTERS = []
    BLEEP_FILTERS = []

    PREVIOUS_FILTER_END = 0
    
    printl("    [blue]↳ [white]Detecting swear words...", end=True)
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

    subprocess.run(FFMPEG_COMMAND, shell=True)
    subprocess.run(CLEAN_UP, shell=True)
    
    return MUSIC_OUTPUT_PATH
