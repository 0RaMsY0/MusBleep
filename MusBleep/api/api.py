import os
import sys
import time
import typer
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile, HTTPException

from utils.printl import printl
from utils.iter_file import iter_file
from src.extract_vocals import extract_vocals
from src.bleep_audio import bleep_vocals

API = FastAPI()

@API.get("/api/v1")
def api_route():
    """
        API main route
    """
    return {
        "status_code": 200,
        "message": "MusBleep API v1"
    }

@API.post("/api/v1/bleep_music", status_code=201)
async def bleep(music_name: str, file: UploadFile = File(...)):
    """
        Bleeps the music that get uploaded
    """
    ALLOWED_FILE_EXTENTIONS = ["mp3", "wav", "webm"]
    SAVE_MUSIC_PATH = f"cache/{music_name if ' ' not in music_name else music_name.replace(' ', '_')}.mp3"

    if music_name.split(".")[-1] not in ALLOWED_FILE_EXTENTIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid file extention, the supported extentions are [`mp3`, `wav`, `webm`]"
        )

    try:
           with open(SAVE_MUSIC_PATH, "wb") as save_music:
               while music_content := file.file.read(1024 * 1024):
                   save_music.write(music_content)
    except Exception as exception:
           print(exception)
           raise HTTPException(
                   status_code=409, 
                    detail=f"Faild to upload `{music_name}`, exception raised: {exception}"
                )
    finally:
           file.file.close()

    # Bleeping the music
    MUSIC_OUTPUT_PATH = bleep_vocals(SAVE_MUSIC_PATH)

    return {
        "status_code": 201,
        "message": f"`{music_name}` uploaded successfully",
        "bleeped_music_path": f"/api/v1/get_music?music_name={SAVE_MUSIC_PATH.replace('cache/', '')}"
    }

@API.get("/api/v1/get_music")
def get_bleeped_music(music_name: str):
    """
        Returns a music file that was requested
    """
    if music_name not in os.listdir("output"):
        raise HTTPException(
            status_code=404,
            detail=f"`{music_name}` not found"
        )
    
    return StreamingResponse(iter_file(f"cache/{music_name}"), media_type="audio/mp3")
